from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(AuthGroup)
@admin.register(AuthGroupPermissions)
@admin.register(AuthPermission)
@admin.register(AuthUser)
@admin.register(AuthUserGroups)
@admin.register(AuthUserUserPermissions)
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
class AuthGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class AuthGroupPermissionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class AuthPermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class AuthUserGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class AuthUserUserPermissionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class BBizareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class BBizpartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class BBizunitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class BCoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class BFactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class BItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class BItemaccntAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class BItemgrpAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class BUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class BWorkcenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class BomDtlAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class BomHdrAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class CbCodeDtlAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class CbCodeHdrAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class CbCostCenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class DjangoAdminLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class DjangoContentType(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class DjangoMigrations(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')
