from .models import *
from rest_framework import serializers


class BcoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BCo
        fields = ('co_cd', 'co_nm', 'co_shnm', 'co_rpr', 'co_type', 'co_div', 'unitcur', 'unitcn')


class BBizareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BBizarea
        fields = ('bizarea_cd', 'co', 'bizarea_nm', 'bizarea_shnm', 'biz_no', 'biz_rpr', 'unitcur', 'unitcn')


class BBizunitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BBizunit
        fields = ('bizunit_cd', 'bizunit_nm', 'bizunit_rmrk')


class BFactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BFactory
        fields = ('factory_cd', 'factory_nm', 'factory_rmrk')


class BWorkcenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BWorkcenter
        fields = ('workcenter_cd', 'workcenter_nm', 'cstctr_id')


class BBizpartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BBizpartner
        fields = ('co_id', 'bizpartner_cd', 'bizpartner_type', 'biz_nm', 'bizpartner_nm', 'unitcur', 'unitcn', 'bizpartner_stat')


class BItemaccntSerializer(serializers.ModelSerializer):
    class Meta:
        model = BItemaccnt
        fields = ('itemaccnt_cd', 'itemaccnt_nm')


class BItemgrpSerializer(serializers.ModelSerializer):
    class Meta:
        model = BItemgrp
        fields = ('itemgrp_cd', 'itemgrp_nm')


class CbCodeHdrSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbCodeHdr
        fields = ('type_cd', 'type_nm')


class CbCodeDtlSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbCodeDtl
        fields = ('type_cd', 'code_cd', 'code_nm')


class CbCostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbCostCenter
        fields = ('cstctr_cd', 'cstctr_nm', 'bizarea_id', 'bizunit_id', 'factory_id', 'cstctr_type', 'cstctr_dir_div')


