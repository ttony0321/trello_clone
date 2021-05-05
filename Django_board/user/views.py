from django.shortcuts import render, redirect
from .forms import LoginForm
# Create your views here.

def home(request):
    return render(request, '../templates/user/home.html')

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, '../templates/user/login.html', {'form': form})

def logout(request):
    if request.session.get('user'): #로그인 되어있을때
        del(request.session['user'])#로그인한 정보

    return redirect('/')