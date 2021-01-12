from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponse, JsonResponse

#
board_path = "board/"


#
# Basic views
def home(request):
    return render(request, 'home.html')


# User Register

def member_register(request):
    return render(request, "registration/member_register.html")


@csrf_exempt
def member_id_check(request):  # 아이디 중복체크
    context = {}

    member_id = request.GET['user_id']
    rs = BUser.objects.filter(user_id=member_id)
    if (len(rs)) > 0:
        context['flag'] = '1'
        context['result_msg'] = '이미 존재하는 아이디입니다.'
    else:
        context['flag'] = '0'
        context['result_msg'] = '사용가능한 아이디입니다.'

    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def member_insert(request):  # 회원등록
    context = {}

    member_id = request.GET['user_id']
    member_pwd = request.GET['psswd']
    member_name = request.GET['user_nm']
    member_phone_num = request.GET['phoneno']
    member_email = request.GET['email']

    rs = BUser.objects.create(user_id=member_id,
                              psswd=member_pwd,
                              user_nm=member_name,
                              email=member_email,
                              phoneno=member_phone_num,
                              usage_fg='1', )

    context['result_msg'] = '회원가입이 완료되었습니다.'

    return JsonResponse(context, content_type="application/json")


# *********************************************************************************************************************
# 거래처 코드 시작
# *********************************************************************************************************************

def b_bizpartner(request):
    context = {}

    # print(typecd)

    rsHeader = BBizpartner.objects.filter(usage_fg='Y')

    context["rsHeader"] = rsHeader

    context["title"] = "거래처"
    context["result_msg"] = "거래처"

    return render(request, board_path + "b_bizpartner.html", context)


@csrf_exempt
def bizpartner_element_insert(request):
    # print("실행완료")
    context = {}

    bizpartnercd = request.GET['bizpartnercd']
    coid = request.GET['coid']
    bizpartnertype = request.GET['bizpartnertype']
    biznm = request.GET['biznm']
    bizpartnernm = request.GET['bizpartnernm']
    cncd = request.GET['cncd']
    curcd = request.GET['curcd']
    bizpartnerstat = request.GET['bizpartnerstat']
    usagefg = 'Y'

    if BBizpartner.objects.filter(bizpartner_cd=bizpartnercd).exists():
        context["flag"] = "1"
        context["result_msg"] = "bizpartner_cd exists..."
        return JsonResponse(context, content_type="application/json")

    if BBizpartner.objects.filter(co_id=coid).exists():
        context["flag"] = "1"
        context["result_msg"] = "co_id exists..."
        return JsonResponse(context, content_type="application/json")

    if BBizpartner.objects.filter(bizpartner_type=bizpartnertype).exists():
        context["flag"] = "1"
        context["result_msg"] = "bizpartner_type exists..."
        return JsonResponse(context, content_type="application/json")

    if BBizpartner.objects.filter(biz_nm=biznm).exists():
        context["flag"] = "1"
        context["result_msg"] = "biz_nm exists..."
        return JsonResponse(context, content_type="application/json")

    if BBizpartner.objects.filter(bizpartner_nm=bizpartnernm).exists():
        context["flag"] = "1"
        context["result_msg"] = "bizpartner_nm exists..."
        return JsonResponse(context, content_type="application/json")

    if BBizpartner.objects.filter(cn_cd=cncd).exists():
        context["flag"] = "1"
        context["result_msg"] = "cn_cd exists..."
        return JsonResponse(context, content_type="application/json")

    if BBizpartner.objects.filter(cur_cd=curcd).exists():
        context["flag"] = "1"
        context["result_msg"] = "cur_cd exists..."
        return JsonResponse(context, content_type="application/json")

    if BBizpartner.objects.filter(bizpartner_stat=bizpartnerstat).exists():
        context["flag"] = "1"
        context["result_msg"] = "bizpartner_stat exists..."
        return JsonResponse(context, content_type="application/json")

    BBizpartner.objects.create(bizpartner_cd=bizpartnercd,
                               co_id=coid,
                               bizpartner_type=bizpartnertype,
                               biz_nm=biznm,
                               bizpartner_nm=bizpartnernm,
                               cn_cd=cncd,
                               cur_cd=curcd,
                               bizpartner_stat=bizpartnerstat,
                               usage_fg=usagefg
                               )

    context["flag"] = "0"
    context["result_msg"] = "bizpartner insert success..."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def bizpartner_element_update(request):
    context = {}

    typeid = request.GET['typeid']
    tvalue = request.GET['tvalue']

    if BBizpartner.objects.filter(type_nm=tvalue).exists():
        context["flag"] = "1"
        context["result_msg"] = "Type name exists..."
        return JsonResponse(context, content_type="application/json")

    rsHeader = BBizpartner.objects.get(id=typeid)
    rsHeader.type_nm = tvalue
    rsHeader.save()

    context["flag"] = "0"
    context["result_msg"] = "Type update success..."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def bizpartner_element_delete(request):
    context = {}

    id = request.GET['id']

    rsHeader = BBizpartner.objects.get(id=id)
    rsHeader.usage_fg = 'N'
    rsHeader.save()

    context["flag"] = "0"
    context["result_msg"] = "Type delete success..."
    return JsonResponse(context, content_type="application/json")


# *********************************************************************************************************************
# 거래처 코드 끝
# *********************************************************************************************************************


def b_co(request):
    return render(request, board_path + "b_co.html")


# **********************************************************************************************************************
# 사업장 코드 시작
# **********************************************************************************************************************

def b_bizarea(request):
    context = {}
    rsHeader = BBizarea.objects.filter(usage_fg='Y')

    strsql = "SELECT b.*,a.*,c.* " + \
             "FROM b_bizarea a " + \
             "LEFT JOIN b_co b ON a.co_id=b.id " + \
             "LEFT JOIN cb_code_dtl c ON a.unit_id=c.id "
    rsBizarea = BBizarea.objects.raw(strsql)
    context["rsBizarea"] = rsBizarea[:100]

    rsCo = BCo.objects.filter()
    rsUnitCur = CbCodeDtl.objects.filter(type_cd='currency', usage_fg='Y')
    rsUnitCn = CbCodeDtl.objects.filter(type_cd='country', usage_fg='Y')
    context["rsCo"] = rsCo
    context["rsUnitCur"] = rsUnitCur
    context["rsUnitCn"] = rsUnitCn
    context["rsHeader"] = rsHeader
    context["title"] = "사업장"
    context["result_msg"] = "사업장"
    return render(request, board_path + "b_bizarea.html", context)


@csrf_exempt
def bizarea_element_insert(request):
    context = {}

    bizareacd = request.GET['bizareacd']
    bizareanm = request.GET['bizareanm']
    bizrpr = request.GET['bizrpr']
    usagefg = 'Y'

    if BBizarea.objects.filter(bizarea_cd=bizareacd).exists():
        context["flag"] = "1"
        context["result_msg"] = "bizarea_cd exists..."
        return JsonResponse(context, content_type="application/json")

    if BBizarea.objects.filter(biz_rpr=bizrpr).exists():
        context["flag"] = "1"
        context["result_msg"] = "biz_rpr exists..."
        return JsonResponse(context, content_type="application/json")

    if BBizarea.objects.filter(bizarea_nm=bizareanm).exists():
        context["flag"] = "1"
        context["result_msg"] = "bizarea_nm exists..."
        return JsonResponse(context, content_type="application/json")

    if BBizarea.objects.filter(biz_rpr=bizrpr).exists():
        context["flag"] = "1"
        context["result_msg"] = "bizpartner_stat exists..."
        return JsonResponse(context, content_type="application/json")

    BBizarea.objects.create(bizarea_cd=bizareacd,
                            bizarea_nm=bizareanm,
                            biz_rpr=bizrpr,
                            usage_fg=usagefg
                            )

    context["flag"] = "0"
    context["result_msg"] = "bizarea insert success..."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def bizarea_element_update(request):
    context = {}

    typeid = request.GET['typeid']
    tvalue = request.GET['tvalue']

    if BBizpartner.objects.filter(type_nm=tvalue).exists():
        context["flag"] = "1"
        context["result_msg"] = "Type name exists..."
        return JsonResponse(context, content_type="application/json")

    rsHeader = BBizarea.objects.get(id=typeid)
    rsHeader.type_nm = tvalue
    rsHeader.save()

    context["flag"] = "0"
    context["result_msg"] = "Type update success..."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def bizarea_element_delete(request):
    context = {}

    id = request.GET['id']

    rsHeader = BBizarea.objects.get(id=id)
    rsHeader.usage_fg = 'N'
    rsHeader.save()

    context["flag"] = "0"
    context["result_msg"] = "Type delete success..."
    return JsonResponse(context, content_type="application/json")


# **********************************************************************************************************************
# 사업장 코드 끝
# ****************************************************************************************************

# *****************************************************************************************
# 사업부 코드 시작
# ****************************************************************************************
def b_bizunit(request):  # 사업부
    context = {}
    rsHeader = BBizunit.objects.filter(usage_fg='Y')
    rsuserid = BUser.objects.filter()  # user_id때문에

    context["title"] = "사업부"
    context["result_msg"] = "사업부"
    context["rsHeader"] = rsHeader
    context["rsuserid"] = rsuserid  # user_id

    return render(request, board_path + "b_bizunit.html", context)


# 정보삽입
@csrf_exempt
def bizunit_element_insert(request):
    context = {}

    bizunitcd = request.GET['bizunitcd']
    bizunitnm = request.GET['bizunitnm']
    bizunitrmrk = request.GET['bizunitrmrk']
    usagefg = 'Y'

    if BBizunit.objects.filter(bizunit_cd=bizunitcd).exists():
        context["flag"] = "1"
        context["result_msg"] = "bizunit_cd exists..."
        return JsonResponse(context, content_type="application/json")

    if BBizunit.objects.filter(bizunit_nm=bizunitnm).exists():
        context["flag"] = "1"
        context["result_msg"] = "bizunit_nm exists..."
        return JsonResponse(context, content_type="application/json")

    if BBizunit.objects.filter(bizunit_rmrk=bizunitrmrk).exists():
        context["flag"] = "1"
        context["result_msg"] = "bizunit_rmrk exists..."
        return JsonResponse(context, content_type="application/json")

    # 생성 부분
    BBizunit.objects.create(bizunit_cd=bizunitcd,
                            bizunit_nm=bizunitnm,
                            bizunit_rmrk=bizunitrmrk,
                            usage_fg=usagefg
                            )

    context["flag"] = "0"
    context["result_msg"] = "bizunit insert success..."
    return JsonResponse(context, content_type="application/json")


# Update기능 미완성 -> 회의 후 항목 설정 예정.
@csrf_exempt
def bizunit_element_update(request):
    context = {}

    typeid = request.GET['typeid']
    tvalue = request.GET['tvalue']

    if BFactory.objects.filter(type_nm=tvalue).exists():
        context["flag"] = "1"
        context["result_msg"] = "Type name exists..."
        return JsonResponse(context, content_type="application/json")

    rsHeader = BBizunit.objects.get(id=typeid)
    rsHeader.type_nm = tvalue
    rsHeader.save()

    context["flag"] = "0"
    context["result_msg"] = "BFactory update success..."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def bizunit_element_delete(request):
    context = {}

    id = request.GET['id']

    rsHeader = BBizunit.objects.get(id=id)
    rsHeader.usage_fg = 'N'
    rsHeader.save()

    context["flag"] = "0"
    context["result_msg"] = "BBizunit elements delete success..."
    return JsonResponse(context, content_type="application/json")


# **********************************************************************************************************************
# 사업부 코드 끝
# ***********************************************************************************************************************

# *********************************************************************************************************************
# 공장 코드 시작
# *********************************************************************************************************************
def b_factory(request):
    context = {}

    # print(typecd)

    rsHeader = BFactory.objects.filter(usage_fg='Y')

    context["rsHeader"] = rsHeader

    context["title"] = "공장"
    context["result_msg"] = "공장"

    return render(request, board_path + "b_factory.html", context)


@csrf_exempt
def factory_element_insert(request):
    context = {}

    factorycd = request.GET['factorycd']
    factorynm = request.GET['factorynm']
    factoryrmrk = request.GET['factoryrmrk']
    usagefg = 'Y'

    if BFactory.objects.filter(factory_cd=factorycd).exists():
        context["flag"] = "1"
        context["result_msg"] = "factory_cd exists..."
        return JsonResponse(context, content_type="application/json")

    if BFactory.objects.filter(factory_nm=factorynm).exists():
        context["flag"] = "1"
        context["result_msg"] = "factory_nm exists..."
        return JsonResponse(context, content_type="application/json")

    if BFactory.objects.filter(factory_rmrk=factoryrmrk).exists():
        context["flag"] = "1"
        context["result_msg"] = "factory_rmrk exists..."
        return JsonResponse(context, content_type="application/json")

    # 생성 부분
    BFactory.objects.create(factory_cd=factorycd,
                            factory_nm=factorynm,
                            factory_rmrk=factoryrmrk,
                            usage_fg=usagefg
                            )

    context["flag"] = "0"
    context["result_msg"] = "factory insert success..."
    return JsonResponse(context, content_type="application/json")


# Update기능 미완성 -> 회의 후 항목 설정 예정.
@csrf_exempt
def factory_element_update(request):
    context = {}

    typeid = request.GET['typeid']
    tvalue = request.GET['tvalue']

    if BFactory.objects.filter(type_nm=tvalue).exists():
        context["flag"] = "1"
        context["result_msg"] = "Type name exists..."
        return JsonResponse(context, content_type="application/json")

    rsHeader = BFactory.objects.get(id=typeid)
    rsHeader.type_nm = tvalue
    rsHeader.save()

    context["flag"] = "0"
    context["result_msg"] = "BFactory update success..."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def factory_element_delete(request):
    context = {}

    id = request.GET['id']

    rsHeader = BFactory.objects.get(id=id)
    rsHeader.usage_fg = 'N'
    rsHeader.save()

    context["flag"] = "0"
    context["result_msg"] = "BFactory elements delete success..."
    return JsonResponse(context, content_type="application/json")


# *********************************************************************************************************************
# 공장 코드 끝
# *********************************************************************************************************************

# *********************************************************************************************************************
# 통합코드관리 코드 시작
# *********************************************************************************************************************

def codemanage(request):
    context = {}

    if 'type_cd' in request.GET:
        typecd = request.GET['type_cd']
        rsCode = CbCodeDtl.objects.filter(type_cd=typecd, usage_fg='Y')
    else:
        typecd = None
        rsCode = None

    context["type_cd"] = typecd

    rsHeader = CbCodeHdr.objects.filter(usage_fg='Y')
    context["rsHeader"] = rsHeader
    context["rsCode"] = rsCode

    return render(request, "board/codemanage.html", context)


@csrf_exempt
def codetype_insert(request):
    context = {}

    typecd = request.GET['typecd']
    typename = request.GET['typename']

    if CbCodeHdr.objects.filter(type_cd=typecd).exists():
        context["flag"] = "1"
        context["result_msg"] = "Type code exists..."
        return JsonResponse(context, content_type="application/json")

    if CbCodeHdr.objects.filter(type_nm=typename).exists():
        context["flag"] = "1"
        context["result_msg"] = "Type name exists..."
        return JsonResponse(context, content_type="application/json")

    CbCodeHdr.objects.create(type_cd=typecd,
                             type_nm=typename,
                             )

    context["flag"] = "0"
    context["result_msg"] = "Type insert success..."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def codetype_update(request):
    context = {}

    typeid = request.GET['typeid']
    tvalue = request.GET['tvalue']

    if CbCodeHdr.objects.filter(type_nm=tvalue).exists():
        context["flag"] = "1"
        context["result_msg"] = "Type name exists..."
        return JsonResponse(context, content_type="application/json")

    rsHeader = CbCodeHdr.objects.get(id=typeid)
    rsHeader.type_nm = tvalue
    rsHeader.save()

    context["flag"] = "0"
    context["result_msg"] = "Type update success..."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def codetype_delete(request):
    context = {}

    typeid = request.GET['typeid']
    rsHeader = CbCodeHdr.objects.get(id=typeid)
    typecd = rsHeader.type_cd

    if CbCodeDtl.objects.filter(type_cd=typecd).exists():
        context["flag"] = "1"
        context["result_msg"] = "하위 코드가 있어 삭제 불가..."
        return JsonResponse(context, content_type="application/json")
    else:
        rsHeader.usage_fg = 'N'
        rsHeader.save()

        context["flag"] = "0"
        context["result_msg"] = "Type delete success..."
        return JsonResponse(context, content_type="application/json")


@csrf_exempt
def code_insert(request):
    context = {}

    typecd = request.GET['typecd']
    codecd = request.GET['codecd']
    codename = request.GET['codename']

    if CbCodeDtl.objects.filter(type_cd=typecd, code_cd=codecd).exists():
        context["flag"] = "1"
        context["result_msg"] = "Code 중복..."
        return JsonResponse(context, content_type="application/json")
    else:
        CbCodeDtl.objects.create(type_cd=typecd,
                                 code_cd=codecd,
                                 cd_nm=codename)

        context["flag"] = "0"
        context["result_msg"] = "Code 등록 성공..."
        return JsonResponse(context, content_type="application/json")


@csrf_exempt
def code_update(request):
    context = {}

    codeid = request.GET['codeid']
    codename = request.GET['codename']

    if CbCodeDtl.objects.filter(cd_nm=codename).exists():
        context["flag"] = "1"
        context["result_msg"] = "Code name exists..."
        return JsonResponse(context, content_type="application/json")

    else:
        rs = CbCodeDtl.objects.get(id=codeid)
        rs.cd_nm = codename
        rs.save()

        context["flag"] = "0"
        context["result_msg"] = "Code update success..."
        return JsonResponse(context, content_type="application/json")


@csrf_exempt
def code_delete(request):
    context = {}

    codeid = request.GET['codeid']

    if CbCodeDtl.objects.get(id=codeid):
        rs = CbCodeDtl.objects.get(id=codeid)
        rs.usage_fg = 'N'
        rs.save()

    context["flag"] = "0"
    context["result_msg"] = "Code deleted... "
    return JsonResponse(context, content_type="application/json")


# 상세정보 html 만들어야함 일단 보류
def code_view(request):
    context = {}

    codeid = request.GET['codeid']
    rsCode = CbCodeDtl.objects.get(id=codeid)

    print(rsCode)

    context["type_cd"] = rsCode.type_cd
    context["code_cd"] = rsCode.code_cd
    context["code_name"] = rsCode.cd_nm

    context["result_msg"] = "Code detail"
    return render(request, "board/codeview.html", context)


# *********************************************************************************************************************
# 통합코드관리 코드 끝
# *********************************************************************************************************************

# *********************************************************************************************************************
# 품목마스터 코드 시작
# *********************************************************************************************************************

def b_item(request):
    context = {}

    context['flag'] = '0'
    context['result_msg'] = '품목코드 관리'

    # rsItem = BItem.objects.filter(usage_fg='Y')

    strSql = "SELECT b.*, c.*, d.*, e.*, a.* " + \
             "FROM (SELECT * FROM b_item WHERE usage_fg = 'Y') a " + \
             "LEFT JOIN b_factory b ON a.factory_id = b.id " + \
             "LEFT JOIN (SELECT id, code_cd AS unit_cd, cd_nm AS unit_name FROM cb_code_dtl WHERE type_cd = 'unit') c  ON a.unit_id = c.id " + \
             "LEFT JOIN b_itemgrp d ON a.itemgrp_id = d.id " + \
             "LEFT JOIN b_itemaccnt e ON a.itemaccnt_id = e.id "

    rsItem = BItem.objects.raw(strSql)

    rsFactory = BFactory.objects.filter()
    rsUnit = CbCodeDtl.objects.filter(type_cd='unit')
    rsItemgrp = BItemgrp.objects.filter()
    rsItemaccnt = BItemaccnt.objects.filter()

    context["rsItem"] = rsItem
    context["rsItemgrp"] = rsItemgrp
    context["rsItemaccnt"] = rsItemaccnt
    context["rsFactory"] = rsFactory
    context["rsUnit"] = rsUnit

    return render(request, 'board/b_item.html', context)


# *********************************************************************************************************************
# 품목마스터 코드 끝
# *********************************************************************************************************************


# *********************************************************************************************************************
# 품목 계정 코드 시작
# *********************************************************************************************************************


def b_itemaccnt(request):
    context = {}

    rsItemaccnt = BItemaccnt.objects.filter(usage_fg='Y')

    context["rsItemaccnt"] = rsItemaccnt

    context["flag"] = "0"
    context["result_msg"] = "품목계정"

    return render(request, 'board/b_itemaccnt.html', context)


@csrf_exempt
def itemaccnt_insert(request):
    context = {}

    itemaccntcd = request.GET['itemaccntcd']
    itemaccntnm = request.GET['itemaccntnm']

    if BItemaccnt.objects.filter(itemaccnt_cd=itemaccntcd).exists():
        context["flag"] = "1"
        context["result_msg"] = "Item account code exists..."
        return JsonResponse(context, content_type="application/json")

    if BItemaccnt.objects.filter(itemaccnt_nm=itemaccntnm).exists():
        context["flag"] = "1"
        context["result_msg"] = "Item account name exists..."
        return JsonResponse(context, content_type="application/json")

    BItemaccnt.objects.create(itemaccnt_cd=itemaccntcd,
                              itemaccnt_nm=itemaccntnm,
                              )

    context["flag"] = "0"
    context["result_msg"] = "Insert success..."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def itemaccnt_delete(request):
    context = {}

    id = request.GET['id']

    if BItemaccnt.objects.get(id=id):
        rs = BItemaccnt.objects.get(id=id)
        rs.usage_fg = 'N'
        rs.save()

    context["flag"] = "0"
    context["result_msg"] = "Delete success..."
    return JsonResponse(context, content_type="application/json")


# *********************************************************************************************************************
# 품목 계정 코드 끝
# *********************************************************************************************************************

# *********************************************************************************************************************
# 품목 그룹 코드 시작
# *********************************************************************************************************************


def b_itemgrp(request):
    context = {}

    rsItemgrp = BItemgrp.objects.filter(usage_fg='Y')

    context["rsItemgrp"] = rsItemgrp

    context["flag"] = "0"
    context["result_msg"] = "품목그룹"

    return render(request, 'board/b_itemgrp.html', context)


@csrf_exempt
def itemgrp_insert(request):
    context = {}

    itemgrpcd = request.GET['itemgrpcd']
    itemgrpnm = request.GET['itemgrpnm']

    if BItemgrp.objects.filter(itemgrp_cd=itemgrpcd).exists():
        context["flag"] = "1"
        context["result_msg"] = "Item group code exists..."
        return JsonResponse(context, content_type="application/json")

    if BItemgrp.objects.filter(itemgrp_nm=itemgrpnm).exists():
        context["flag"] = "1"
        context["result_msg"] = "Item account name exists..."
        return JsonResponse(context, content_type="application/json")

    BItemgrp.objects.create(itemgrp_cd=itemgrpcd,
                            itemgrp_nm=itemgrpnm,
                            )

    context["flag"] = "0"
    context["result_msg"] = "Insert success..."
    return JsonResponse(context, content_type="application/json")


@csrf_exempt
def itemgrp_delete(request):
    context = {}

    id = request.GET['id']

    if BItemgrp.objects.get(id=id):
        rs = BItemgrp.objects.get(id=id)
        rs.usage_fg = 'N'
        rs.save()

    context["flag"] = "0"
    context["result_msg"] = "Delete success..."
    return JsonResponse(context, content_type="application/json")


# *********************************************************************************************************************
# 품목 그룹 코드 끝
# *********************************************************************************************************************

def b_user(request):
    return render(request, 'b_user.html')


def b_workcenter(request):
    return render(request, 'b_workcenter.html')


def bom_hdr(request):
    return render(request, 'b_bizarea.html')


def bom_dtl(request):
    return render(request, 'b_bizarea.html')


def cb_code_hdr(request):
    return render(request, 'cb_code_hdr.html')


def cb_code_dtl(request):
    return render(request, 'cb_code_dtl.html')


def cb_cost_center(request):
    return render(request, 'cb_cost_center.html')
