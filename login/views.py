from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .froms import UserForm, AddNewProduct, Modify_fix, Modify_Product, addNewCustomer, addRepairProduct
from . import models
from .models import Trproduct, Tproduct, Prproduct, fix_tr_report, fix_tp_report,customer
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from datetime import datetime



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
    Trdatabase = Trproduct.objects.all()
    Tdatabase = Tproduct.objects.all()
    Prdatabase = Prproduct.objects.all()
    FixTrDatabase = fix_tr_report.objects.all()
    FixTpDatabase = fix_tp_report.objects.all()
    edit_form_fix = Modify_fix()
    return render(request,'login/index.html',context={'Trdatabase': Trdatabase ,'Tdatabase':Tdatabase,'Prdatabase':Prdatabase,'FixTrDatabase':FixTrDatabase,'FixTpDatabase':FixTpDatabase,'edit_form_fix':edit_form_fix})

def add_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('Product_id')
        product_name = request.POST.get('Product_name')
        Product_no = request.POST.get('Product_no')
        Product_Price = request.POST.get('Product_Price')
        Product_time = request.POST.get('Product_time')
        company = request.POST.get('Product_Company')
        # print(product_id)
        # print(product_name)
        # print(Product_time)
        # print(Product_no)
        # print(Product_Price)
        # print(company)
        if product_id == '' or product_name =='' or Product_no=='' or Product_Price=='' or Product_time=='':
            return render(request,'login/addnewproduct.html',{'ret':'error!'})
        if company == 'Trproduct':
            models.Trproduct.objects.create(tr_product_id=product_id, tr_product_name=product_name,
                                            tr_product_num=Product_no, tr_product_price=Product_Price,
                                            tr_product_time=Product_time)
            message = "add successful!"
        elif company == 'Tproduct':
            models.Tpproduct.objects.create(tp_product_id=product_id, tp_product_name=product_name,
                                            tp_product_num=Product_no, tp_product_price=Product_Price,
                                            tp_product_time=Product_time)
            message = "add successful!"
        elif company == 'Prproduct':
            models.Prproduct.objects.create(pr_product_id=product_id, pr_product_name=product_name,
                                            pr_product_num=Product_no, pr_product_price=Product_Price,
                                            pr_product_time=Product_time)
            message = "add successful!"
        else:
            message = "error!"
    #     return redirect('/login/index.html')
    # else:
    #     return render(request, '/login/index.html')
    product_form = AddNewProduct()
    return render(request,'login/addnewproduct.html',locals())

def del_fix_tr_product(request,id):
    models.fix_tr_report.objects.filter(id=id).delete()
    return redirect('/index/')

def del_fix_tp_product(request,id):
    models.fix_tp_report.objects.filter(id=id).delete()
    return redirect('/index/')

def modify_product(request,id):
    produt_obj = models.Trproduct.objects.filter(id=id).first()
    print(produt_obj)
    if request.method == 'POST':
        product_id = request.POST.get('tr product id')
        product_name = request.POST.get('tr product name')
        product_state = request.POST.get('tr product state')
        if product_id == '' or product_name == '' or product_state == '':
            return render(request, 'login/add.html', {'ret': 'error!'})
        models.Trproduct.objects.filter(id=id).update(tp_product_id = product_id, tr_product_name = product_name, tr_product_description = product_state)
        return redirect('/login/index.html')
    else:
        return render(request, '/login/index.html')

def TrSubpage(request):
    return render(request,'login/TRsubpage.html',locals())

def TrProductList(request):
    Trdatabase = Trproduct.objects.all()
    modify_form = Modify_Product
    return render(request,'login/TRproductList.html',context={'Trdatabase':Trdatabase,'modify_form':modify_form})


def TrProductStockOut(request):
    Trdatabase = Trproduct.objects.all()
    Customerdatabase = customer.objects.all()
    if request.method == "POST":
        s = request.POST.getlist("check")
        n = request.POST.getlist('quantity')
        custom_info = request.POST.copy()
        #generatePDF(request,custom_info )
        #return redirect('/generate_pdf/', {'custom_info': custom_info})
    return render(request, 'login/TRproductOut.html', custom_info,context={'Trdatabase': Trdatabase,'Customerdatabase':Customerdatabase})

def pdfdownload(request):
    # Create the HttpResponse object
    response = HttpResponse(content_type='application/pdf')

    # This line force a download
    response['Content-Disposition'] = 'attachment; filename="1.pdf"'

    # READ Optional GET param
    get_param = request.GET.get('name', 'World')

    # Generate unique timestamp
    ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

    p = canvas.Canvas(response)

    # Write content on the PDF
    p.drawString(100, 500, "Hello " + get_param + " (Dynamic PDF) - " + ts )

    # Close the PDF object.
    p.showPage()
    p.save()

    # Show the result to the user
    return response

# def edit_fix(request,id):
#     edit_form_fix = Modify_fix()
#     return render(request,'/login/index.html',locals())

def addrepairproduct(request):
    repair_form = addRepairProduct()
    return render(request, 'login/addrepairproduct.html', locals())

def addnewcustomer(request):
    customer_form = addNewCustomer()
    return render(request,'login/addnewcustomer.html',locals())

def generatePDF(request,customerifo):
    return render('login/generate_pdf.html',{'customerifo':customerifo})
