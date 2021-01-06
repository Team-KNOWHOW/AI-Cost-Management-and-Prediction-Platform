from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.home, name='home'),
    path('b_bizarea/', views.b_bizarea, name='b_bizarea_list'),#######
    path('b_bizpartner/', views.b_bizpartner, name='b_bizpartner_list'),
    path('b_bizunit/', views.b_bizunit, name='b_bizunit_list'),#####
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
]
