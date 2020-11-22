from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Corporation, Establishment, Department, Factory, Workshop, Item, CostCenter, CostElementAccount, \
    Client, BOM


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'


# List view
class CorporationLV(ListView):
    model = Corporation
    template_name = 'board/corporation.html'
    context_object_name = 'corporations'


class EstablishmentLV(ListView):
    model = Establishment
    template_name = 'board/establishment.html'
    context_object_name = 'establishments'


class DepartmentLV(ListView):
    model = Department
    template_name = 'board/department.html'
    context_object_name = 'departments'


class FactoryLV(ListView):
    model = Factory
    template_name = 'board/factory.html'
    context_object_name = 'factories'


class WorkshopLV(ListView):
    model = Workshop
    template_name = 'board/workshop.html'
    context_object_name = 'workshops'


class ItemLV(ListView):
    model = Item
    template_name = 'board/item.html'
    context_object_name = 'items'


class CostCenterLV(ListView):
    model = CostCenter
    template_name = 'board/cost_center.html'
    context_object_name = 'cost_centers'


class CostElementAccountLV(ListView):
    model = CostElementAccount
    template_name = 'board/cost_element_account.html'
    context_object_name = 'cost_element_accounts'


class ClientLV(ListView):
    model = Client
    template_name = 'board/client.html'
    context_object_name = 'clients'


class BomLV(ListView):
    model = BOM
    template_name = 'board/bom.html'
    context_object_name = 'boms'
