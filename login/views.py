from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .froms import UserForm,AddNewProduct
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


def index(request):
    data = Trproduct.objects.all()
    data1 = Tproduct.objects.all()
    data2 = Prproduct.objects.all()
    return render(request,'login/index.html',context={'data':data,'data1':data1,'data2':data2})

def add_product(request):
    # if request.method == 'POST':
    #     product_form = AddNewProduct(request.POST)
    #     message ="Please Check Input!"
    #     if product_form.is_valid():
    #
    #         product_id = request.POST.get('tr product id')
    #         product_name = request.POST.get('tr product name')
    #         product_state = request.POST.get('tr product state')
    #         if product_id == '' or product_name =='' or product_state=='':
    #             return render(request,'login/addnewproduct.html',{'ret':'error!'})
    #     models.Trproduct.objects.create(tr_product = product_id, tr_product_name = product_name, tr_product_description = product_state)
    #     return redirect('/login/index.html')
    # else:
    #     return render(request, '/login/index.html')

    product_form = AddNewProduct()
    return render(request, 'login/addnewproduct.html', locals())

def del_product(request,id):
        print(id)
        models.Trproduct.objects.filter(id=id).delete()
        return redirect('/login/index.html')



def modify_product(request,id):
    produt_obj = models.Trproduct.objects.filter(id=id).first()
    print(produt_obj)
    if request.method == 'POST':
        product_id = request.POST.get('tr product id')
        product_name = request.POST.get('tr product name')
        product_state = request.POST.get('tr product state')
        if product_id == '' or product_name == '' or product_state == '':
            return render(request, 'login/add.html', {'ret': 'error!'})
        models.Trproduct.objects.filter(id=id).update(tr_product = product_id, tr_product_name = product_name, tr_product_description = product_state)
        return redirect('/login/index.html')
    else:
        return render(request, '/login/index.html')
