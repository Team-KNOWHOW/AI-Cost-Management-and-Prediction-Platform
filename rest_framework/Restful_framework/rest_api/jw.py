# multi-step bayesianlstm


def dataLoader():

    dbCon = pymysql.connect(host='223.194.46.212', user='root', password='12345!', database='knowhow',
                            charset='utf8', autocommit=True,
                            cursorclass=pymysql.cursors.DictCursor)

    # Sales, variable cost, fixed cost , material cost(매출액, 변동비, 고정비, 재료비)
    y1 = '''SELECT cc_costbill.periodym_cd  AS version_id,
        cc_costbill.proamt_unit*cc_costbill.proq AS y
        ,cc_costbill.ic_dlvc+ cc_costbill.ic_ohdvc +cc_costbill.ic_idlc+cc_costbill.ic_idohc AS x1,
        cc_costbill.ic_dlfc + cc_costbill.ic_ohdfe +cc_costbill.ic_ohdfd AS x2,
        cc_costbill.uc_srw AS x3

        FROM cc_costbill;'''

    curs = dbCon.cursor()
    curs.execute(y1)
    result = curs.fetchall()

    # make DB table into pandas dataframe
    df = pd.DataFrame(result)
    df_new = df.groupby(['version_id'], as_index=False)['x1', 'x2', 'x3', 'y'].agg('sum')
    return df_new

##############################차후 모듈화 해야될 것..To create the dataset for later use#####
def creat_dataset_x(data, lagTerm=1):
    # lagTerm: How many previous timestemp's data will be used.
    dataX =[]
    for i in range(len(data) - lagTerm -2):
        cache = data[i:(i+lagTerm)]
        dataX.append(cache)
    return np.array(dataX)
def creat_dataset_y(data, lagTerm=1):
    dataY = []
    for i in range(len(data) - lagTerm -2):
        cache = data[(i+lagTerm):(i+lagTerm+3)]
        dataY.append(cache)
    return np.array(dataY)
def fitModel(numEpoch,batchSize,X,y,valX,valy,callBack):
    tf.keras.backend.clear_session()
    # Start to build the model.
    inp = Input(shape=(X.shape[1], X.shape[2]))
    n_outputs = y.shape[1]
    x = inp
    x = LSTM(200, return_sequences=True,input_shape=(X.shape[1], X.shape[2]),dropout=0.4, recurrent_dropout = 0.4)(x)
    x = LSTM(100, return_sequences=False)(x)
    # Local reparameterization LSTM again
    mean = Dropout(rate=0.4)(x,training=True)
    mean = Dense(n_outputs)(mean)

    model = Model(inp,mean)

    model.compile(optimizer='adam', loss='mse')
    hist = model.fit(X,y,epochs = numEpoch, batch_size=8,  validation_data=(valX, valy), callbacks=callBack)
    loss = hist.history['loss'][-1]

    return model,loss

#########################################################################

def modelTrain():   #모델 훈련 및 저장 함수
    df_new = dataLoader()

    date = df_new['version_id'].astype(str)
    kdate = [datetime.strptime(d, '%Y%m') for d in date]
    df_new['version_id'] = kdate

    df_new = df_new.set_index(['version_id'])

    # # LSTM is sensitive to scale, thus a scaler is necessary.
    scaler = RobustScaler()

    trans_dfnew = df_new
    ycol = ["y"]  # 종속변수
    xcol = ['x1', 'x2', 'x3', 'y']  # 전체 열
    xxcol = ['x1', 'x2', 'x3']  # 독립변수
    y_prices_unscaled = df_new["y"]
    trans_dfnew[xxcol] = scaler.fit_transform(trans_dfnew[xxcol])  # x 정규화 시킨거 변경해줌
    y_scaler = RobustScaler()

    trans_dfnew[ycol] = y_scaler.fit_transform(trans_dfnew[ycol])  #

    dataset = trans_dfnew.values
    dataset = dataset.astype('float32')

    n_train_time = int(len(df_new) * 0.90)
    train = dataset[:n_train_time, :]
    test = dataset[n_train_time:, :]

    train_x, train_y = train[:, :-1], train[:, -1]
    test_x, test_y = test[:, :-1], test[:, -1]

    # train the model
    look_back = 3
    trainX = creat_dataset_x(train_x, look_back)
    trainY = creat_dataset_y(train_y, look_back)
    testX = creat_dataset_x(test_x, look_back)
    testY = creat_dataset_y(test_y, look_back)

    # Set a valida set to avoid overfitting
    validX = trainX[201:]
    validY = trainY[201:]
    trainX = trainX[:200]
    trainY = trainY[:200]

    # Early stop callback function.
    early_stopping_cb = keras.callbacks.EarlyStopping(patience=15, restore_best_weights=True)

    #Real training
    theModel, ELBO = fitModel(300, 1, trainX, trainY, validX, validY, [early_stopping_cb])

    theModel.save('static/model/khmodel.h5')
    #여기까지 모델 트레이닝 & 저장 완료 to static/model/khmodel.h5

def mainChartPredict():
    df_new = dataLoader()

    date = df_new['version_id'].astype(str)
    kdate = [datetime.strptime(d, '%Y%m') for d in date]
    df_new['version_id'] = kdate

    df_new = df_new.set_index(['version_id'])

    # # LSTM is sensitive to scale, thus a scaler is necessary.
    scaler = RobustScaler()

    trans_dfnew = df_new
    ycol = ["y"]  # 종속변수
    xcol = ['x1', 'x2', 'x3', 'y']  # 전체 열
    xxcol = ['x1', 'x2', 'x3']  # 독립변수
    y_prices_unscaled = df_new["y"]
    trans_dfnew[xxcol] = scaler.fit_transform(trans_dfnew[xxcol])  # x 정규화 시킨거 변경해줌
    y_scaler = RobustScaler()

    trans_dfnew[ycol] = y_scaler.fit_transform(trans_dfnew[ycol])  #

    dataset = trans_dfnew.values
    dataset = dataset.astype('float32')

    n_train_time = int(len(df_new) * 0.90)
    train = dataset[:n_train_time, :]
    test = dataset[n_train_time:, :]

    train_x, train_y = train[:, :-1], train[:, -1]
    test_x, test_y = test[:, :-1], test[:, -1]

    recent_threeMonth =test_x[-3:].reshape(1,3,3)

    theModel = keras.models.load_model('static/model/khmodel.h5')
    allpredict = [theModel.predict(recent_threeMonth) for _ in tqdm(range(100))]
    # print(k)

    allpredict = np.array(allpredict)

    predvalue = np.mean(allpredict, axis=0).flatten()  # predictive mean
    # print(m)
    variance = np.var(allpredict, axis=0).flatten()  # epistemic uncertainty
    # print(v)

    variance = variance.squeeze()
    predvalue = predvalue.reshape(3, )
    # shape맞춰주고

    # invert predictions
    ep_up = predvalue + 2 * variance ** 0.5
    ep_down = predvalue - 2 * variance ** 0.5

    # invertransform형태로 변환(3,1)
    predvalue = predvalue.reshape(-1, 1)
    ep_up = ep_up.reshape(-1, 1)
    ep_down = ep_down.reshape(-1, 1)
    realPredict = y_scaler.inverse_transform(predvalue)
    epUp = y_scaler.inverse_transform(ep_up)
    epDown = y_scaler.inverse_transform(ep_down)

    # unsqueeze한번 해주고
    realPredict = realPredict.reshape(3, )
    rpDown = epDown.reshape(3, )
    rpUp = epUp.reshape(3, )


def simulatorLoader(): # 모델 읽고 1월값 받은 후 -> 예측 3개월(2월 3월 4월) 출력함수
    # [ 3개 output(array) return : 예측값(3개월치) , 최대 예측(3개월치), 최소 예측(3개월치) ]
# userInput 부분 처리해야 됌.
    df_new = dataLoader()

    date = df_new['version_id'].astype(str)
    kdate = [datetime.strptime(d, '%Y%m') for d in date]
    df_new['version_id'] = kdate

    df_new = df_new.set_index(['version_id'])

    # # LSTM is sensitive to scale, thus a scaler is necessary.
    scaler = RobustScaler()

    trans_dfnew = df_new
    ycol = ["y"]  # 종속변수
    xcol = ['x1', 'x2', 'x3', 'y']  # 전체 열
    xxcol = ['x1', 'x2', 'x3']  # 독립변수
    y_prices_unscaled = df_new["y"]
    trans_dfnew[xxcol] = scaler.fit_transform(trans_dfnew[xxcol])  # x 정규화 시킨거 변경해줌
    y_scaler = RobustScaler()

    trans_dfnew[ycol] = y_scaler.fit_transform(trans_dfnew[ycol])  #

    dataset = trans_dfnew.values
    dataset = dataset.astype('float32')

    n_train_time = int(len(df_new) * 0.90)
    train = dataset[:n_train_time, :]
    test = dataset[n_train_time:, :]

    train_x, train_y = train[:, :-1], train[:, -1]
    test_x, test_y = test[:, :-1], test[:, -1]

    ###요거가 인풋받을거!!!!
    userInput = np.array(1.05 * test_x[-1]).astype('float32')

    # 3개월 예측 코드
    a = np.append(test_x[-2:], userInput)
    a = a.reshape(3, 3)
    # 앞에서 a에 input모양 으로 변환완료함
    a = a.reshape(1, 3, 3)

    theModel = keras.models.load_model('static/model/khmodel.h5')
    k = [theModel.predict(a) for _ in tqdm(range(100))]
    #print(k)

    k = np.array(k)

    m = np.mean(k, axis=0).flatten()  # predictive mean
    #print(m)
    v = np.var(k, axis=0).flatten()  # epistemic uncertainty
    #print(v)

    v = v.squeeze()
    m = m.reshape(3, )
    # shape맞춰주고

    # invert predictions
    ep_up = m + 2 * v ** 0.5
    ep_down = m - 2 * v ** 0.5

    # invertransform형태로 변환(3,1)
    m = m.reshape(-1, 1)
    ep_up = ep_up.reshape(-1, 1)
    ep_down = ep_down.reshape(-1, 1)
    testPredict = y_scaler.inverse_transform(m)
    epUp = y_scaler.inverse_transform(ep_up)
    epDown = y_scaler.inverse_transform(ep_down)

    # unsqueeze한번 해주고
    testPredict = testPredict.reshape(3, )
    epDown = epDown.reshape(3, )
    epUp = epUp.reshape(3, )

    return testPredict, epUp, epDown
