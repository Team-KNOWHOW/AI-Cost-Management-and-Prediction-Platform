from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponse, JsonResponse

#
board_path = "board/"
#
# Create your views here.
def home(request):
    return render(request, 'home.html')


def b_bizarea(request):
    return render(request, 'b_bizarea.html')

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

    return render(request, board_path+"b_bizpartner.html", context)

@csrf_exempt
def bizpartner_element_insert(request):
    #print("실행완료")
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

def b_bizunit(request):
    return render(request, 'b_bizunit.html')


def b_co(request):
    return render(request, board_path+"b_co.html")


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

    return render(request, board_path+"b_factory.html", context)

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


def b_item(request):
    return render(request, 'b_item.html')


def b_itemaccnt(request):
    return render(request, 'b_itemaccnt.html')


def b_itemgrp(request):
    return render(request, 'b_itemgrp.html')


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