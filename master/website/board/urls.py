from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    # Basic urls 항목
    path('', views.home, name='home'),
    path('b_bizarea/', views.b_bizarea, name='b_bizarea_list'),
    path('b_bizpartner/', views.b_bizpartner, name='b_bizpartner_list'),
    path('b_bizunit/', views.b_bizunit, name='b_bizunit_list'),
    path('b_co/', views.b_co, name='b_co_list'),
    path('b_factory/', views.b_factory, name='b_factory_list'),
    path('b_item/', views.b_item, name='b_item_list'),
    path('b_itemaccnt/', views.b_itemaccnt, name='b_itemaccnt_list'),
    path('b_itemgrp/', views.b_itemgrp, name='b_itemgrp_list'),
    path('b_user/', views.b_user, name='b_user_list'),
    path('b_workcenter/', views.b_workcenter, name='b_workcenter_list'),
    path('bom_hdr/', views.bom_hdr, name='bom_hdr_list'),
    path('cb_code_hdr/', views.cb_code_hdr, name='cb_code_hdr_list'),
    path('cb_cost_center/', views.cb_cost_center, name='cb_cost_center_list'),
    path('codemanage/', views.codemanage, name='codemanage'),

    # 공장 기능 항목
    path('b_factory/factory_element_insert', views.factory_element_insert, name="factory_element_insert"),
    path('b_factory/factory_element_update', views.factory_element_update, name="factory_element_update"),
    path('b_factory/factory_element_delete', views.factory_element_delete, name="factory_element_delete"),

    # 거래처 기능 항목
    path('b_bizpartner/bizpartner_element_insert', views.bizpartner_element_insert, name="bizpartner_element_insert"),
    path('b_bizpartner/bizpartner_element_update', views.bizpartner_element_update, name="bizpartner_element_update"),
    path('b_bizpartner/bizpartner_element_delete', views.bizpartner_element_delete, name="bizpartner_element_delete"),


    #통합코드 헤더 기능 항목
    path('codemanage/codetype_insert', views.codetype_insert, name="codetype_insert"),
    path('codemanage/codetype_update', views.codetype_update, name="codetype_update"),
    path('codemanage/codetype_delete', views.codetype_delete, name="codetype_delete"),

    #통합코드 디테일 기능 항목
    path('codemanage/code_insert', views.code_insert, name='code_insert'),
    path('codemanage/code_update', views.code_update, name='code_update'),
    path('codemanage/code_delete', views.code_delete, name='code_delete'),
    path('codemanage/code_view', views.code_view, name='code_view'),

]
