from django.shortcuts import render,redirect

def index(request):
    pass
    return render(request,'login/templates/index.html')

def login(request):
    pass
    return render(request,'login/templates/login.html')

def register(request):
    pass
    return render(request,'login/templates/register.html')

def logout(request):
    pass
    return redirect('/index/')