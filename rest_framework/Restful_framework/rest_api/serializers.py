from .models import *
from rest_framework import serializers


class BcoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BCo
        fields = ('id', 'co_cd', 'co_nm', 'co_shnm', 'co_rpr', 'co_type', 'co_div', 'unitcur', 'unitcn')
