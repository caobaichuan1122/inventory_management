from django.shortcuts import render,redirect
from .froms import UserForm
from . import models
from .models import Trproduct, Tproduct, Prproduct


# def index(request):
#     data = Trproduct.objects.all()
#     return render(request,'login/index.html',context={'data':data})

def login(request):
    # if request.session.get('is_login',None):
    #     return redirect('/index/') #sing in page

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "please check！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')  #s in page
                else:
                    message = "password error！"
            except:
                message = "user error！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    pass
    return render(request,'login/register.html')

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    # request.session.flush()
    del request.session['is_login']
    del request.session['user_id']
    del request.session['user_name']
    return redirect("/login/")

# def Trcheck(request):
#     if request.method == 'POST':
#         tr_product = request.POST['Product ID']
#         tr_product_name = request.POST['Product Name']
#         tr_product_description = request.POST['Product State']
#
#         #Trproduct write
#         Trproduct.objects.create(tr_product = tr_product, tr_product_name = tr_product_name, tr_product_description = tr_product_description)

#
# def datacheck(request):
#     data = Trproduct.objects.all()
#     return render(request,'login/index.html',context={'data':data})

def index(request):
    data = Trproduct.objects.all()
    data1 = Tproduct.objects.all()
    data2 = Prproduct.objects.all()
    return render(request,'login/index.html',context={'data':data,'data1':data1,'data2':data2})
