from django.shortcuts import render,redirect
from .froms import UserForm
from login import models


def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "Please check！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "password error！"
            except:
                message = "account error！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())

def register(request):
    pass
    return render(request,'login/register.html')

def logout(request):
    pass
    return redirect('/index/')