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

