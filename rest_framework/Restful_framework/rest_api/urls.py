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
]
