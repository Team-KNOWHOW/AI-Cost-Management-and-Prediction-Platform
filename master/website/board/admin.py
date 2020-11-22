from django.contrib import admin
from .models import Corporation, Establishment, Department, Factory, Workshop, Item, CostCenter, CostElementAccount, \
    Client, BOM


# Register your models here.

@admin.register(Corporation)
@admin.register(Establishment)
@admin.register(Department)
@admin.register(Factory)
@admin.register(Workshop)
@admin.register(Item)
@admin.register(CostCenter)
@admin.register(CostElementAccount)
@admin.register(Client)
@admin.register(BOM)
class CorporationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class CostCenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class CostElementAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')


class BOMAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('name', 'content')
