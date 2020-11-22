from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.HomeView.as_view(), name='main'),
    path('corporation/', views.CorporationLV.as_view(), name='corporation_list'),
    path('establishment/', views.EstablishmentLV.as_view(), name='establishment_list'),
    path('department/', views.DepartmentLV.as_view(), name='department_list'),
    path('factory/', views.FactoryLV.as_view(), name='factory_list'),
    path('workshop/', views.WorkshopLV.as_view(), name='workshop_list'),
    path('item/', views.ItemLV.as_view(), name='item_list'),
    path('cost_center/', views.CostCenterLV.as_view(), name='cost_center_list'),
    path('cost_element_account/', views.CostElementAccountLV.as_view(), name='cost_element_account_list'),
    path('client/', views.ClientLV.as_view(), name='client_list'),
    path('bom/', views.BomLV.as_view(), name='bom_list'),
]
