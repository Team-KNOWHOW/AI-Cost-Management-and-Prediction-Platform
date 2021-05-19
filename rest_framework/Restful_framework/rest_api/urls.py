"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'rest_api'

urlpatterns = [

    # 1단계 기준정보 CRUD API

    path('corporations', views.co_list, name='co_list'),
    path('corporations/<int:pk>', views.co_detail, name='co_detail'),

    path('bizareas', views.bizarea_list, name='bizarea_list'),
    path('bizareas/<int:pk>', views.bizarea_detail, name='bizarea_detail'),

    path('bizunits', views.bizunit_list, name='bizunit_list'),
    path('bizunits/<int:pk>', views.bizunit_detail, name='bizunit_detail'),

    path('factories', views.factory_list, name='factory_list'),
    path('factories/<int:pk>', views.factory_detail, name='factory_detail'),

    path('workcenters', views.workcenter_list, name='workcenter_list'),
    path('workcenters/<int:pk>', views.workcenter_detail, name='workcenter_detail'),

    path('bizpartners', views.bizpartner_list, name='bizpartner_list'),
    path('bizpartners/<int:pk>', views.bizpartner_detail, name='bizpartner_detail'),

    path('item-accounts', views.itemaccnt_list, name='itemaccnt_list'),
    path('item-accounts/<int:pk>', views.itemaccnt_detail, name='itemaccnt_detail'),

    path('item-groups', views.itemgrp_list, name='itemgrp_list'),
    path('item-groups/<int:pk>', views.itemgrp_detail, name='itemgrp_detail'),

    path('code-headers', views.code_hdr_list, name='code_hdr_list'),
    path('code-headers/<int:pk>', views.code_hdr_detail, name='code_hdr_detail'),

    path('code-details', views.code_dtl_list, name='code_dtl_list'),
    path('code-details/<int:pk>', views.code_dtl_detail, name='code_dtl_detail'),

    path('costcenters', views.cstctr_list, name='cstctr_list'),
    path('costcenters/<int:pk>', views.cstctr_detail, name='cstctr_detail'),

    path('items', views.item_list, name='item_list'),
    path('items/<int:pk>', views.item_detail, name='item_detail'),

    path('cost-element-accounts', views.costeleaccnt_list, name='costeleaccnt_list'),
    path('cost-element-accounts/<int:pk>', views.costeleaccnt_detail, name='costeleaccnt_detail'),

    path('costbill', views.costbill_list, name='costbill_list'),
    path('costbill/<int:pk>', views.costbill_detail, name='costbill_detail'),

    # 2단계 Excel Upload, Download API
    path('cc-manu-cost-if', views.cc_manucost_if, name='cc_manucost_if_template'),
    path('cc-material-cost-if', views.cc_materialcost_if, name='cc_materialcost_if_template'),
    path('cc-item-per-manu-cost-if', views.cc_itempermanucost_if, name='cc_itempermanucost_template'),
    path('cc-product-cost-payment-if', views.cc_productcostpayment_if, name='cc_productcostpayment_if_template'),

    # 2단계 API DB 연결 upload
    path('db-name', views.db_name, name='coneected_db_name'),

    path('cc-manu-cost-if-db', views.cc_manucost_if_db, name='cc_manucost_if_db_upload'),
    #path('cc-material-cost-if-db', views.cc_materialcost_if_db, name='cc_materialcost_if_db_upload'),
    #path('cc-item-per-manu-cost-if-db', views.cc_itempermanucost_if_db, name='cc_itempermanucost_db_upload'),
    #path('cc-product-cost-payment-if-db', views.cc_productcostpayment_if_db, name='cc_productcostpayment_if_db_upload'),

    # 3단계 분석 결과 data API
    path('ca-prediction_main', views.ca_prediction_main, name='ca_prediction_main_result'),
    path('ca-prediction_simulation', views.ca_prediction_simul, name='ca_prediction_simul_result'),

    # 3단계 분석 기능 API
    path('trained-data', views.train_data, name='train_data'),
    path('predicted-data', views.predict_data, name='predict_data'),
]
