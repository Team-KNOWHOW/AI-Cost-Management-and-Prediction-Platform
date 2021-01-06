from django.shortcuts import render


# Create your views here.
# from .models import BBizunit,BUser,BCo,BBizarea
from .models import BBizunit, BBizarea, BUser,BCo

def home(request):
    return render(request, 'home.html')
def b_co(request):
    return render(request, 'b_co.html')

def b_bizarea(request):#사업장
    return render(request, 'b_bizarea.html')

def b_bizunit(request):#사업부
    context={}
    rsbizunit=BBizunit.objects.filter()
    rsuserid=BUser.objects.filter()
    context["rsbizunit"]=rsbizunit
    context["rsuserid"]=rsuserid
    return render(request, 'bizunit.html',context)





def b_factory(request):
    return render(request, 'b_factory.html')


def b_item(request):
    return render(request, 'b_item.html')


def b_itemaccnt(request):
    return render(request, 'b_itemaccnt.html')


def b_itemgrp(request):
    return render(request, 'b_itemgrp.html')


def b_user(request):
    return render(request, 'b_user.html')


def b_workcenter(request):
    return render(request, 'b_workcenter.html')


def bom_hdr(request):
    return render(request, 'b_bizarea.html')


def bom_dtl(request):
    return render(request, 'b_bizarea.html')


def cb_code_hdr(request):
    return render(request, 'cb_code_hdr.html')


def cb_code_dtl(request):
    return render(request, 'cb_code_dtl.html')


def cb_cost_center(request):
    return render(request, 'cb_cost_center.html')

def b_bizpartner(request):
    return render(request, 'b_bizpartner.html')

