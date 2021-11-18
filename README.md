# AI Cost Management and Prediction Platform

<br>
의사 결정 지원(DSS)을 위한 '인공지능 원가(손익/예산) 관리 및 예측 플랫폼'
<br><br>

### : Main Services
#### :heavy_check_mark: 원가 통합 관리
#### :heavy_check_mark: 전년/전월 , 당기사용/당기 투입 정보 차트 시각화
#### :heavy_check_mark: 외부요인(환율,유가 등) 자동 크롤링
#### :heavy_check_mark: 3개월 후 매출액 예측(Prediction)
#### :heavy_check_mark: 내부 요인 변경을 통한 예측 시뮬레이션(Simulation)
#### :heavy_check_mark: 예측에 대한 해석정보(Explainer)

<br><br>
## 시연 영상 🔽🔽
### [![AI Cost Management and Prediction Platform](http://img.youtube.com/vi/N9mTU6sIqak/0.jpg)](https://youtu.be/N9mTU6sIqak?t=0s)  

#### Youtube: https://www.youtube.com/watch?v=N9mTU6sIqak

***
<br/>


# 프로젝트 요약
  - 제조회사를 타겟팅한 프로젝트로 제품을 생성하는데 사용되는 비용인 재료비, 노무비, 경비를 체계적으로 관리 
  - 원가를 구성하는 변동비 고정비 재료비의 과거 데이터를 시계열 분석을 통해 향후 3개월 매출액을 예측하여 기업의 매출액 예측 지원
  - 원가 예측 Simulation을 통해 고정비, 변동비, 재료비의 변동에 따라 매출 예측액을 확인하여 경영권자가 최선의 선택을 하도록 의사결정을 지원해주는 것이 KNOWHOW 원가 예측 플렛폼의 핵심
<br/>
# 애플리케이션 설명

<ul>
<li>회사의 기준정보 관리를 입력한다. (법인정보, 사업장, 사업부, 공장, 작업장, 품목, BOM...etc)</li>
<li>매달 재무부에서 만드는 제조비용 I/F, 재료비I/F, 품목별 제조비용 I/F, 제품원가수불 I/F를 DB연결 혹은 엑섹을 통해 업로드를 한다. (업로드된 데이터는 년월/version에 따라 확인 가능하고 계속 축적되어 조회가 가능)</li>
<li>업로드된 4가지 I/F를 통해 자동적으로 원가계산서가 완성되어 한달간 기업이 제품생산에 사용한 기초제공품 비용, 당기투입 비용, 당기사용 비용, 기말 제공품 비용을 계산. 계산된 원가계산서를 통해 한달간 매출액과 비용을 확인할 수 있다.</li>
<li>메인화면 죄측의 '원가분석'을 클릭하여 막대 그래프와 선그래프 차트를 통해 1년 주기로 당기투입, 당기사용 금액을 확인</li>
<li>마찬가지로 '원가분석' 클릭후 '전년/월대비'를 클릭하면 전년, 전월 대비 성장률을 비교하여 회사 매출 변화 트렌드를 보여준다.</li>
<li>좌측의 '기준정보관리', '원가기준정보', '원가계산'의 I/F를 전부 업로드 하면 메인 화면에서 시계열 차트 생성하여 매출액의 변화 확인이 가능하다.</li>
<li>향후 3개월 예측을 하기위해서는 메인 화면에 '학습' 버튼 클릭한다. '완료'라는 알림이 뜨기 전까지 대기하도록 한다. '완료' 알림이 생성 되면 메인 화면에 '예측'을 클릭, '완료'라는 알림이 뜨면 메인화면에 3개월 예측치가 나타난다.
(기간이 길경우 메인화면의 '조회시작 시점'을 클릭하여 그래프를 늘리고 줄일 수 있다.)</li>
<li>메인화면의 'Simulate' 화면 클릭시 화면에 오늘의 환률, 기준금리를 알수 있고 우측에 '변동비', '고정비', '재료비' 3가지 원가 요소들을 변동시켜 다음 3개월을 예측한다. 이를 통해 어떤 원가 요소가 매출액에 영향을 끼치는지 인사이트를 얻을 수 있다.</li>
<li>메인화면에 'Explanation' 이미지를 클릭한다. 그러면 시계열 데이터 분석시 사용된 내부변수인 '변동비', '고정비', '재료비'와 외부변수인 '환률'과 '금리'가 매출액어 어떤 긍정적 영향 혹은 부정적 영향을 끼치는 지 차트가 생성되어 더 쉽게 인사이트를 얻을 수 있다.</li>
</ul>

## 소스코드 실행 방법

### 1. 배포 버전 실행
 - http://223.194.46.212:8756/ 접속
 - 테스트 아이디 : pyh123
 - 비밀번호 : 1234
 - 로그인 후 왼쪽 탭에서 원하는 기능 실행
### 2. 개발모드로 로컬에서 실행
 - 시스템 버전을 전부 다운 받은후 작업을 진행 ( secrets.json 요청 : pyhpyh0670@gmail.com)
 - Pycharm 실행
 - Anaconda 가상환경 구성(Python 3.7)
 - 가상환경 실행
 - 다운로드 받은 소스로 새 프로젝트 구성.
 - AI-Cost-Management-and-Prediction-Platform/rest_framework 이동
 - pip3 install -r requirements.txt 명령어을 통해 패키지 설치
 - AI-Cost-Management-and-Prediction-Platform/rest_framework/Restful_framework 이동
 - python manage.py runserver 8080 (8080 포트 번호로 API 서버 실행)
 - Pycharm Open project로 동일한 프로젝트 New Window로 열기 (가상환경은 동일)
 - AI-Cost-Management-and-Prediction-Platform/master/website 이동
 - python manage.py runserver (template 화면 보여주는 django 서버 실행)
 - http://127.0.0.1:8000/ 접속

