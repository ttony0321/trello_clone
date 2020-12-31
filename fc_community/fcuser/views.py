from django.shortcuts import render, redirect
from .models import Fcuser
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse


# Create your views here.


def register(request):  # 2가지 접근방식 1. 주소 직접 입력하여 접근, 2. 회원 등록 하여 접근
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}
        if not(username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력 하세요'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                user_name=username,
                useremail = useremail,
                password=make_password(password)    #암호화
            )
            fcuser.save()
        return render(request, 'register.html', res_data)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        #모든 값을 입력했는지, 비밀번호가 같은지 확인

        res_data = {}
        if not(username and password):
            res_data['error'] = "모든 값을 입력하세요"
        else:
            #아이디 같은지 확인
            fcuser = Fcuser.objects.get(username=username)
            if check_password(password, fcuser.password):
                request.session['user'] = fcuser.id
                return redirect("/")    #홈으로 이동
            else:
                res_data['error'] = '비밀번호를 틀렸습니다.'

        return render(request, 'login.html')
def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.user_name)

    return HttpResponse('home!')
