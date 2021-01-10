from django.shortcuts import render
#from ..board.models import BUser
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Main View
def main_view(request):
    return render(request, "login.html")


# User Register

def member_register(request):
    return render(request, "member_register.html")


"""@csrf_exempt
def member_id_check(request):
    context = {}

    member_id = request.GET['user_id']
    rs = BUser.objects.filter(user_id=member_id)
    if(len(rs))>0:
        context['flag'] = '1'
        context['result_msg'] = '이미 존재하는 아이디입니다.'
    else:
        context['flag'] = '0'
        context['result_msg'] = '사용가능한 아이디입니다.'

    return JsonResponse(context, content_type="application/json")
"""