from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import exceptions
from openpyxl import Workbook
import pymysql
from django.conf import settings

MYDB = getattr(settings, "DATABASES", None)
MYDB_NAME = MYDB["default"]["NAME"]
MYDB_USER = MYDB["default"]["USER"]
MYDB_PWD = MYDB["default"]["PASSWORD"]
MYDB_HOST = MYDB["default"]["HOST"]
dbCon = pymysql.connect(host=MYDB_HOST, user=MYDB_USER, passwd=MYDB_PWD, database=MYDB_NAME)


@api_view(['GET', 'POST'])
@csrf_exempt
def co_list(request):
    if request.method == 'GET':
        query_set = BCo.objects.all()
        serializer = BcoSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        if BCo.objects.filter(co_cd=data['co_cd'], usage_fg='Y').exists():
            raise exceptions.ParseError("DuplicateCode")

        serializer = BcoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def co_detail(request, pk):
    obj = BCo.objects.get(id=pk)

    if request.method == 'GET':  # 현재 화면에선 개별조회 미지원.
        serializer = BcoSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BcoSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
@csrf_exempt
def bizarea_list(request):
    if request.method == 'GET':
        query_set = BBizarea.objects.all()
        serializer = BBizareaSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        if BBizarea.objects.filter(bizarea_cd=data['bizarea_cd'], usage_fg='Y').exists():
            raise exceptions.ParseError("DuplicateCode")

        serializer = BBizareaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def bizarea_detail(request, pk):
    obj = BBizarea.objects.get(id=pk)

    if request.method == 'GET':  # 현재 화면에선 개별조회 미지원.
        serializer = BBizareaSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BBizareaSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
@csrf_exempt
def bizunit_list(request):
    if request.method == 'GET':
        query_set = BBizunit.objects.all()
        serializer = BBizunitSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        if BBizunit.objects.filter(bizunit_cd=data['bizunit_cd'], usage_fg='Y').exists():
            raise exceptions.ParseError("DuplicateCode")

        serializer = BBizunitSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def bizunit_detail(request, pk):
    obj = BBizunit.objects.get(id=pk)

    if request.method == 'GET':  # 현재 화면에선 개별조회 미지원.
        serializer = BBizunitSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BBizunitSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
@csrf_exempt
def factory_list(request):
    if request.method == 'GET':
        query_set = BFactory.objects.all()
        serializer = BFactorySerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        if BFactory.objects.filter(factory_cd=data['factory_cd'], usage_fg='Y').exists():
            raise exceptions.ParseError("DuplicateCode")

        serializer = BFactorySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def factory_detail(request, pk):
    obj = BFactory.objects.get(id=pk)

    if request.method == 'GET':  # 현재 화면에선 개별조회 미지원.
        serializer = BFactorySerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BFactorySerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
@csrf_exempt
def workcenter_list(request):
    if request.method == 'GET':
        query_set = BWorkcenter.objects.all()
        serializer = BWorkcenterSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        if BWorkcenter.objects.filter(workcenter_cd=data['workcenter_cd'], usage_fg='Y').exists():
            raise exceptions.ParseError("DuplicateCode")

        serializer = BWorkcenterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def workcenter_detail(request, pk):
    obj = BWorkcenter.objects.get(id=pk)

    if request.method == 'GET':  # 현재 화면에선 개별조회 미지원.
        serializer = BWorkcenterSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BWorkcenterSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
@csrf_exempt
def bizpartner_list(request):
    if request.method == 'GET':
        query_set = BBizpartner.objects.all()
        serializer = BBizpartnerSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        if BBizpartner.objects.filter(bizpartner_cd=data['bizpartner_cd'], usage_fg='Y').exists():
            raise exceptions.ParseError("DuplicateCode")

        serializer = BBizpartnerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def bizpartner_detail(request, pk):
    obj = BBizpartner.objects.get(id=pk)

    if request.method == 'GET':  # 현재 화면에선 개별조회 미지원.
        serializer = BBizpartnerSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BBizpartnerSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        # print(serializer.errors.values())
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
@csrf_exempt
def itemaccnt_list(request):
    if request.method == 'GET':
        query_set = BItemaccnt.objects.all()
        serializer = BItemaccntSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        if BItemaccnt.objects.filter(itemaccnt_cd=data['itemaccnt_cd'], usage_fg='Y').exists():
            raise exceptions.ParseError("DuplicateCode")

        serializer = BItemaccntSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def itemaccnt_detail(request, pk):
    obj = BItemaccnt.objects.get(id=pk)

    if request.method == 'GET':  # 현재 화면에선 개별조회 미지원.
        serializer = BItemaccntSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BItemaccntSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
@csrf_exempt
def itemgrp_list(request):
    if request.method == 'GET':
        query_set = BItemgrp.objects.all()
        serializer = BItemgrpSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        if BItemgrp.objects.filter(itemgrp_cd=data['itemgrp_cd'], usage_fg='Y').exists():
            raise exceptions.ParseError("DuplicateCode")

        serializer = BItemgrpSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def itemgrp_detail(request, pk):
    obj = BItemgrp.objects.get(id=pk)

    if request.method == 'GET':  # 현재 화면에선 개별조회 미지원.
        serializer = BItemgrpSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BItemgrpSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
@csrf_exempt
def code_hdr_list(request):
    if request.method == 'GET':
        query_set = CbCodeHdr.objects.all()
        serializer = CbCodeHdrSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        if CbCodeHdr.objects.filter(type_cd=data['type_cd'], usage_fg='Y').exists():
            raise exceptions.ParseError("Duplicate Type Code")

        if CbCodeHdr.objects.filter(type_nm=data['type_nm'], usage_fg='Y').exists():
            raise exceptions.ParseError("Duplicate Type Name")

        serializer = CbCodeHdrSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def code_hdr_detail(request, pk):
    obj = CbCodeHdr.objects.get(id=pk)

    if request.method == 'GET':  # 현재 화면에선 개별조회 미지원.
        serializer = CbCodeHdrSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)

        if CbCodeHdr.objects.filter(type_nm=data['type_nm'], usage_fg='Y').exists():
            raise exceptions.ParseError("Duplicate Type Name")

        serializer = CbCodeHdrSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        if CbCodeDtl.objects.filter(type_cd=obj.type_cd, usage_fg='Y').exists():
            raise exceptions.ParseError("Can't delete root code")

        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
@csrf_exempt
def code_dtl_list(request):
    if request.method == 'GET':
        query_set = CbCodeDtl.objects.all()
        serializer = CbCodeDtlSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        if CbCodeDtl.objects.filter(cd_nm=data['cd_nm'], usage_fg='Y').exists():
            raise exceptions.ParseError("Duplicate Code Name")

        serializer = CbCodeDtlSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def code_dtl_detail(request, pk):
    obj = CbCodeDtl.objects.get(id=pk)

    if request.method == 'GET':  # 현재 화면에선 개별조회 미지원.
        serializer = CbCodeDtlSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)

        if CbCodeDtl.objects.filter(cd_nm=data['cd_nm'], usage_fg='Y').exists():
            raise exceptions.ParseError("Duplicate Code Name")

        serializer = CbCodeDtlSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
@csrf_exempt
def cstctr_list(request):
    if request.method == 'GET':
        query_set = CbCostCenter.objects.all()
        serializer = CbCostCenterSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        if CbCostCenter.objects.filter(cstctr_cd=data['cstctr_cd'], usage_fg='Y').exists():
            raise exceptions.ParseError("Duplicate Code")

        if CbCostCenter.objects.filter(cstctr_nm=data['cstctr_nm'], usage_fg='Y').exists():
            raise exceptions.ParseError("Duplicate Name")

        serializer = CbCostCenterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def cstctr_detail(request, pk):
    obj = CbCostCenter.objects.get(id=pk)

    if request.method == 'GET':  # 현재 화면에선 개별조회 미지원.
        serializer = CbCostCenterSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)

        serializer = CbCostCenterSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
@csrf_exempt
def item_list(request):
    if request.method == 'GET':
        query_set = BItem.objects.all()
        serializer = BItemSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = BItemSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def item_detail(request, pk):
    obj = BItem.objects.get(id=pk)

    if request.method == 'GET':  # 현재 화면에선 개별조회 미지원.
        serializer = BItemSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)

        serializer = BItemSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
@csrf_exempt
def costeleaccnt_list(request):
    if request.method == 'GET':
        query_set = BCosteleaccnt.objects.all()
        serializer = BCosteleaccntSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        if BCosteleaccnt.objects.filter(pl_cd=data['pl_cd'], usage_fg='Y').exists():
            raise exceptions.ParseError("Duplicate PL Code")

        if BCosteleaccnt.objects.filter(accnt_cd=data['accnt_cd'], usage_fg='Y').exists():
            raise exceptions.ParseError("Duplicate Account Code")

        serializer = BCosteleaccntSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def costeleaccnt_detail(request, pk):
    obj = BCosteleaccnt.objects.get(id=pk)

    if request.method == 'GET':  # 현재 화면에선 개별조회 미지원.
        serializer = BCosteleaccntSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)

        serializer = BCosteleaccntSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
@csrf_exempt
def cc_manucost_if(request):
    if request.method == 'GET':  # Excel Template Download

        strsql1 = "SHOW TABLES LIKE 'cc_manucost_if'"

        cursor1 = dbCon.cursor()
        cursor1.execute(strsql1)
        rsTmp = cursor1.fetchone()
        cursor1.close()

        rsColumns = None
        if rsTmp:
            strsql1 = "SHOW FULL COLUMNS FROM cc_manucost_if"

            cursor2 = dbCon.cursor()
            cursor2.execute(strsql1)
            rsColumns = cursor2.fetchall()
            cursor2.close()

            idx = 1

            bookin = Workbook()
            sheet_in = bookin.active

            for i in rsColumns:
                sheet_in.cell(row=1, column=idx).value = i[1]
                sheet_in.cell(row=2, column=idx).value = i[8]
                idx += 1

            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="manucost.xlsx"'

            bookin.save(response)
            bookin.close()

        return response

    elif request.method == 'POST':  # Excel Template Upload
        file = request.get('input_file')

        print(file)

        #if BCosteleaccnt.objects.filter(pl_cd=data['pl_cd'], usage_fg='Y').exists():
            #raise exceptions.ParseError("Duplicate PL Code")

        #if BCosteleaccnt.objects.filter(accnt_cd=data['accnt_cd'], usage_fg='Y').exists():
           #raise exceptions.ParseError("Duplicate Account Code")

    return JsonResponse(status=201)


@api_view(['GET', 'POST'])
@csrf_exempt
def costbill_list(request):
    if request.method == 'GET':
        query_set = CcCostBill.objects.raw("SELECT * FROM cc_costbill")
        serializer = CcCostBillSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def costbill_detail(request, pk):
    obj = CbCostCenter.objects.get(id=pk)

    if request.method == 'GET':  # 현재 화면에선 개별조회 미지원.
        serializer = CbCostCenterSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)

        if CbCostCenter.objects.filter(cstctr_nm=data['cstctr_nm'], usage_fg='Y').exists():
            raise exceptions.ParseError("Duplicate Name")

        serializer = CbCostCenterSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


def ca_prediction(request):
    if request.method == 'GET':  # 가장 최근에 생성된 row 겍체를 반환.
        obj = CaPrediction.objects.last()
        serializer = CaPredictionSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        obj = CaPrediction.objects.filter(variableperc_cost=data['variableperc_cost'],
                                          fixedperc_cost=data['fixedperc_cost'],
                                          materialperc_cost=data['materialperc_cost'])
        if obj.exists():  # 변동비, 고정비, 재료비가 같은 row가 존재하면 해당 row 객체 반환.
            serializer = CaPredictionSerializer(obj)
            return JsonResponse(serializer.data, status=201)

        serializer = CaPredictionSerializer(data=data)  # 새로운 row 객체를 생성해서 변동비, 고정비, 재료비 속성에 입력 받은 값을 넣음.

        if serializer.is_valid():
            serializer.save()
            print("모델 동작 시키는 view 함수실행.")
            return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)
