from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    # 화면 urls 항목
    path('', views.home, name='home'),
    path('b_bizarea/', views.b_bizarea, name='b_bizarea_list'),
    path('b_bizpartner/', views.b_bizpartner, name='b_bizpartner_list'),
    path('b_bizunit/', views.b_bizunit, name='b_bizunit_list'),
    path('b_co/', views.b_co, name='b_co_list'),
    path('b_factory/', views.b_factory, name='b_factory_list'),
    path('b_item/', views.b_item, name='b_item_list'),
    path('b_workcenter/', views.b_workcenter, name='b_workcenter_list'),
    path('b_bom/', views.b_bom, name='b_bom_list'),
    path('cb_cost_center/', views.cb_cost_center, name='cb_cost_center_list'),
    path('codemanage/', views.codemanage, name='codemanage'),
    path('b_itemaccnt/', views.b_itemaccnt, name='b_itemaccnt'),
    path('b_itemgrp/', views.b_itemgrp, name='b_itemgrp'),
    path('b_costeleaccnt/',views.b_costeleaccnt, name='b_costeleaccnt'),
    path('cc_manucost_if', views.cc_manucost_if, name='cc_manucost_if'),
    path('cc_materialcost_if', views.cc_materialcost_if, name='cc_materialcost_if'),
    path('cc_itempermanucost_if', views.cc_itempermanucost_if, name='cc_itempermanucost_if'),
    path('cc_productcostpayment_if', views.cc_productcostpayment_if, name='cc_productcostpayment_if'),
    path('cc_costbill_if', views.cc_costbill_if, name='cc_costbill_if'),
    path('cc_costbill1_if', views.cc_costbill1_if, name='cc_costbill1_if'),
    path('chart_if', views.chart_if, name='chart_if'),
    path('chart1', views.chart1, name='chart1'),
    path('chart2', views.chart2, name='chart2'),
    path('chart3', views.chart3, name='chart3'),
    path('simulate', views.simulate, name='simulate'),


    # 사용자 관리
    path('member_register', views.member_register, name="member_register"),
    path('member_id_check', views.member_id_check, name="member_id_check"),
    path('member_insert', views.member_insert, name="member_insert"),
    path('member_login', views.member_login, name="member_login"),
    path('member_logout', views.member_logout, name="member_logout"),
    path('member_check', views.member_check, name="member_check"),
    path('member_pwd_check', views.member_pwd_check, name="member_pwd_check"),
    path('member_edit', views.member_edit, name="member_edit"),
    path('member_update', views.member_update, name="member_update"),

    # BOM 기능 항목
    path('b_bom/bom_create', views.bom_create, name="bom_create"),
    path('b_bom/bomitem_read', views.bomitem_read, name="bomitem_read"),
    path('b_bom/bomitem_pick', views.bomitem_pick, name="bomitem_pick"),
    path('b_bom/bom_update', views.bom_update, name="bom_update"),


]
