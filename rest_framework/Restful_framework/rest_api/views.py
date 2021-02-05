from django.shortcuts import render
from .models import BCo
from rest_framework import viewsets
from .serializers import *


class Bco(viewsets.ModelViewSet):
    queryset = BCo.objects.all()
    serializer_class = BcoSerializer
