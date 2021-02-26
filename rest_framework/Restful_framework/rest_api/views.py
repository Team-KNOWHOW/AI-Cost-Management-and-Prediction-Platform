from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import exceptions


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






