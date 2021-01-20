from django.shortcuts import render


def main_view(request):

    context = {}
    if request.session.has_key('id'):  # 로그인 되어있는 상태인지 체크.
        member_no = request.session['id']
        member_id = request.session['user_id']
    else:
        member_no = None
        member_id = None

    context["id"] = member_no
    context["user_id"] = member_id

    return render(request, "registration/login.html", context)
