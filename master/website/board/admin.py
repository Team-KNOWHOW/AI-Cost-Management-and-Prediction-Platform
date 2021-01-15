from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(BBizarea)
@admin.register(BBizpartner)
@admin.register(BBizunit)
@admin.register(BCo)
@admin.register(BFactory)
@admin.register(BItem)
@admin.register(BItemaccnt)
@admin.register(BItemgrp)
@admin.register(BUser)
@admin.register(BWorkcenter)
@admin.register(BomDtl)
@admin.register(BBom)
@admin.register(CbCodeDtl)
@admin.register(CbCodeHdr)
@admin.register(CbCostCenter)
@admin.register(DjangoAdminLog)
@admin.register(DjangoContentType)
@admin.register(DjangoMigrations)
class BBizareaAdmin(admin.ModelAdmin):
    list_display = ('id',)
    #list_filter = ('updt_dt',)
    #search_fields = ('name', 'content')


class BBizpartnerAdmin(admin.ModelAdmin):
    list_display = ('id',)
    #list_filter = ('updt_dt',)
    # search_fields = ('name', 'content')


class BBizunitAdmin(admin.ModelAdmin):
    list_display = ('id',)
    #list_filter = ('updt_dt',)
    # search_fields = ('name', 'content')


class BCoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    #list_filter = ('updt_dt',)
    # search_fields = ('name', 'content')


class BFactoryAdmin(admin.ModelAdmin):
    list_display = ('id',)
    #list_filter = ('updt_dt',)
    # search_fields = ('name', 'content')


class BItemAdmin(admin.ModelAdmin):
    list_display = ('id',)
    #list_filter = ('updt_dt',)
    # search_fields = ('name', 'content')


class BItemaccntAdmin(admin.ModelAdmin):
    list_display = ('id',)
    #list_filter = ('updt_dt',)
    # search_fields = ('name', 'content')


class BItemgrpAdmin(admin.ModelAdmin):
    list_display = ('id',)
    #list_filter = ('updt_dt',)
    # search_fields = ('name', 'content')


class BUserAdmin(admin.ModelAdmin):
    list_display = ('id',)
    #list_filter = ('updt_dt',)
    # search_fields = ('name', 'content')


class BWorkcenterAdmin(admin.ModelAdmin):
    list_display = ('id',)
    #list_filter = ('updt_dt',)
    # search_fields = ('name', 'content')


class BomDtlAdmin(admin.ModelAdmin):
    list_display = ('id',)
    #list_filter = ('updt_dt',)
    # search_fields = ('name', 'content')


class BomHdrAdmin(admin.ModelAdmin):
    list_display = ('id',)
    #list_filter = ('updt_dt',)
    # search_fields = ('name', 'content')


class CbCodeDtlAdmin(admin.ModelAdmin):
    list_display = ('id',)
    #list_filter = ('updt_dt',)
    # search_fields = ('name', 'content')


class CbCodeHdrAdmin(admin.ModelAdmin):
    list_display = ('id',)
    #list_filter = ('updt_dt',)
    # search_fields = ('name', 'content')


class CbCostCenterAdmin(admin.ModelAdmin):
    list_display = ('id',)
    #list_filter = ('updt_dt',)
    # search_fields = ('name', 'content')
