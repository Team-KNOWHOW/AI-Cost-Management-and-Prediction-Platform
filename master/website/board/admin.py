from django.contrib import admin

from .models import *

# from .models import Corporation, Establishment, Department, Factory, Workshop, Item, CostCenter, CostElementAccount, \
#     Client, BOM



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
@admin.register(BomHdr)
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

# @admin.register(Corporation)
# @admin.register(Establishment)
# @admin.register(Department)
# @admin.register(Factory)
# @admin.register(Workshop)
# @admin.register(Item)
# @admin.register(CostCenter)
# @admin.register(CostElementAccount)
# @admin.register(Client)
# @admin.register(BOM)
# class CorporationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'modify_dt')
#     list_filter = ('modify_dt',)
#     search_fields = ('name', 'content')
#
#
# class EstablishmentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'modify_dt')
#     list_filter = ('modify_dt',)
#     search_fields = ('name', 'content')
#
#
# class DepartmentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'modify_dt')
#     list_filter = ('modify_dt',)
#     search_fields = ('name', 'content')
#
#
# class FactoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'modify_dt')
#     list_filter = ('modify_dt',)
#     search_fields = ('name', 'content')
#
#
# class WorkshopAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'modify_dt')
#     list_filter = ('modify_dt',)
#     search_fields = ('name', 'content')
#
#
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'modify_dt')
#     list_filter = ('modify_dt',)
#     search_fields = ('name', 'content')
#
#
# class CostCenterAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'modify_dt')
#     list_filter = ('modify_dt',)
#     search_fields = ('name', 'content')
#
#
# class CostElementAccountAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'modify_dt')
#     list_filter = ('modify_dt',)
#     search_fields = ('name', 'content')
#
#
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'modify_dt')
#     list_filter = ('modify_dt',)
#     search_fields = ('name', 'content')
#
#
# class BOMAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'modify_dt')
#     list_filter = ('modify_dt',)
#     search_fields = ('name', 'content')
