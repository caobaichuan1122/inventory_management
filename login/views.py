from django.contrib.staticfiles import finders
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .froms import UserForm, AddNewProduct, Modify_fix, Modify_Product, addNewCustomer, addRepairProduct
from . import models
from .models import Trproduct, Tproduct, Prproduct, fix_tr_report, fix_tp_report,customer
from reportlab.pdfgen import canvas
from datetime import datetime
# from weasyprint import HTML
# from django.core.files.storage import FileSystemStorage
from io import StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from html import escape
from django.utils.text import slugify
from django.template.loader import render_to_string
# import pdfkit
# from django_pdfkit import PDFView
# from easy_pdf.views import PDFTemplateView


import os

from django.conf import settings


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

def repair_list(request):
    FixTrDatabase = fix_tr_report.objects.all()
    FixTpDatabase = fix_tp_report.objects.all()
    edit_form_fix = Modify_fix()
    return render(request,'login/TotalRepairList.html',context={'FixTrDatabase':FixTrDatabase,'FixTpDatabase':FixTpDatabase,'edit_form_fix':edit_form_fix})

def TpRepairList(request):
    FixTpDatabase = fix_tp_report.objects.all()
    edit_form_fix = Modify_fix()
    return render(request, 'login/TPrepairList.html',context={'FixTpDatabase': FixTpDatabase,'edit_form_fix': edit_form_fix})

def TrRepairList(request):
    FixTrDatabase = fix_tr_report.objects.all()
    edit_form_fix = Modify_fix()
    return render(request,'login/TRrepairList.html',context={'FixTrDatabase':FixTrDatabase,'edit_form_fix':edit_form_fix})

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
    product_form = AddNewProduct()
    return render(request,'login/addnewproduct.html',locals())

def del_fix_tr_product(request,id):
    models.fix_tr_report.objects.filter(id=id).delete()
    return redirect('/index/')

def del_fix_tp_product(request,id):
    models.fix_tp_report.objects.filter(id=id).delete()
    return redirect('/index/')

def modify_fix_product(request,id):
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

def TpSubpage(request):
    return render(request,'login/TPsubpage.html',locals())

def PrSubpage(request):
    return render(request,'login/PRsubpage.html',locals())

def TrProductList(request):
    Trdatabase = Trproduct.objects.all()
    modify_form = Modify_Product()
    return render(request,'login/TRproductList.html',context={'Trdatabase':Trdatabase,'modify_form':modify_form})

def TpProductList(request):
    Tpdatabase = Tproduct.objects.all()
    modify_form = Modify_Product()
    return render(request,'login/TPproductList.html',context={'Tpdatabase':Tpdatabase,'modify_form':modify_form})

def PrProductList(request):
    Prdatabase = Prproduct.objects.all()
    modify_form = Modify_Product()
    return render(request,'login/PRproductList.html',context={'Prdatabase':Prdatabase,'modify_form':modify_form})

def TrProductStockOut(request):
    Trdatabase = Trproduct.objects.all()
    Customerdatabase = customer.objects.all()
    return render(request, 'login/TRproductOut.html',context={'Trdatabase': Trdatabase,'Customerdatabase':Customerdatabase})

def TpProductStockOut(request):
    Tpdatabase = Tproduct.objects.all()
    Customerdatabase = customer.objects.all()
    return render(request, 'login/TPproductOut.html',context={'Tpdatabase': Tpdatabase,'Customerdatabase':Customerdatabase})

def TpRepairStockOut(request):
    TpFixdatabase = fix_tp_report.objects.all()
    Customerdatabase = customer.objects.all()
    return render(request, 'login/TpRepairOut.html',context={'TpFixdatabase': TpFixdatabase,'Customerdatabase':Customerdatabase})

def TrRepairStockOut(request):
    TrFixdatabase = fix_tr_report.objects.all()
    Customerdatabase = customer.objects.all()
    return render(request, 'login/TrRepairOut.html',context={'TrFixdatabase': TrFixdatabase, 'Customerdatabase': Customerdatabase})


def PrProductStockOut(request):
    Prdatabase = Prproduct.objects.all()
    Customerdatabase = customer.objects.all()
    return render(request, 'login/PRproductOut.html',context={'Prdatabase': Prdatabase,'Customerdatabase':Customerdatabase})



def addrepairproduct(request):
    repair_form = addRepairProduct()
    return render(request, 'login/addrepairproduct.html', locals())

def addnewcustomer(request):
    customer_form = addNewCustomer()
    return render(request,'login/addnewcustomer.html',locals())

def generatePDF(request):
    Trdatabase = Trproduct.objects.all()
    Customerdatabase = customer.objects.all().values()
    if request.method == "POST":
        company_id = request.POST.get('company_id')
        product_id = request.POST.getlist("check")
        product_quantity = list(filter(None,request.POST.getlist('quantity')))
        customerid = request.POST.get('customer')
        Invoice_date = request.POST.get('Invoicedate')
        Delivery_date = request.POST.get('Deliverydate')
        Invoice_no = request.POST.get('invoice_no')
        Note = request.POST.get('Note')
        Delivery_No = request.POST.get('DeliveryNo')
        Delivery_Term = request.POST.get('DeliveryTerm')
        customer_info = customer.objects.filter(customer_id=customerid).values()
        product_list = Trproduct.objects.filter(id__in=product_id).values()
        sum_quantity = str(sum([int(n) for n in product_quantity]))
        return render(request,'login/generate_pdf.html',context={'company_id':company_id,'Delivery_No':Delivery_No,'Delivery_Term':Delivery_Term,'product_list':product_list,'product_quantity':product_quantity,'customer_info':customer_info,'Invoice_date':Invoice_date,'Delivery_date':Delivery_date,'Invoice_no':Invoice_no,'Note':Note,'sum_quantity':sum_quantity})
    else:
        return render(request, 'login/TRproductOut.html',context={'Trdatabase': Trdatabase, 'Customerdatabase': Customerdatabase})

def generatePDF_tp(request):
    Tpdatabase = Tproduct.objects.all()
    Customerdatabase = customer.objects.all().values()
    if request.method == "POST":
        company_id = request.POST.get('company_id')
        product_id = request.POST.getlist("check")
        product_quantity = list(filter(None,request.POST.getlist('quantity')))
        customerid = request.POST.get('customer')
        Invoice_date = request.POST.get('Invoicedate')
        Delivery_date = request.POST.get('Deliverydate')
        Invoice_no = request.POST.get('invoice_no')
        Note = request.POST.get('Note')
        Delivery_No = request.POST.get('DeliveryNo')
        Delivery_Term = request.POST.get('DeliveryTerm')
        customer_info = customer.objects.filter(customer_id=customerid).values()
        product_list = Tproduct.objects.filter(id__in=product_id).values()
        sum_quantity = str(sum([int(n) for n in product_quantity]))
        return render(request,'login/generate_pdf.html',context={'company_id':company_id,'Delivery_No':Delivery_No,'Delivery_Term':Delivery_Term,'product_list':product_list,'product_quantity':product_quantity,'customer_info':customer_info,'Invoice_date':Invoice_date,'Delivery_date':Delivery_date,'Invoice_no':Invoice_no,'Note':Note,'sum_quantity':sum_quantity})
    else:
        return render(request, 'login/TPproductOut.html',context={'Tpdatabase': Tpdatabase, 'Customerdatabase': Customerdatabase})

def generatePDF_pr(request):
    Prdatabase = Prproduct.objects.all()
    Customerdatabase = customer.objects.all().values()
    if request.method == "POST":
        company_id = request.POST.get('company_id')
        product_id = request.POST.getlist("check")
        product_quantity = list(filter(None,request.POST.getlist('quantity')))
        customerid = request.POST.get('customer')
        Invoice_date = request.POST.get('Invoicedate')
        Delivery_date = request.POST.get('Deliverydate')
        Invoice_no = request.POST.get('invoice_no')
        Note = request.POST.get('Note')
        Delivery_No = request.POST.get('DeliveryNo')
        Delivery_Term = request.POST.get('DeliveryTerm')
        customer_info = customer.objects.filter(customer_id=customerid).values()
        product_list = Prproduct.objects.filter(id__in=product_id).values()
        sum_quantity = str(sum([int(n) for n in product_quantity]))
        return render(request,'login/generate_pdf.html',context={'company_id':company_id,'Delivery_No':Delivery_No,'Delivery_Term':Delivery_Term,'product_list':product_list,'product_quantity':product_quantity,'customer_info':customer_info,'Invoice_date':Invoice_date,'Delivery_date':Delivery_date,'Invoice_no':Invoice_no,'Note':Note,'sum_quantity':sum_quantity})
    else:
        return render(request, 'login/TPproductOut.html',context={'Prdatabase': Prdatabase, 'Customerdatabase': Customerdatabase})



def generatePDF_fix_tp(request):
    TpFixdatabase = fix_tp_report.objects.all()
    Customerdatabase = customer.objects.all()
    if request.method == "POST":
        company_id = request.POST.get('company_id')
        product_id = request.POST.getlist("check")
        customerid = request.POST.get('customer')
        Invoice_date = request.POST.get('Invoicedate')
        Delivery_date = request.POST.get('Deliverydate')
        Invoice_no = request.POST.get('invoice_no')
        Note = request.POST.get('Note')
        Delivery_No = request.POST.get('DeliveryNo')
        Delivery_Term = request.POST.get('DeliveryTerm')
        customer_info = customer.objects.filter(customer_id=customerid).values()
        product_list = fix_tp_report.objects.filter(id__in=product_id).values()
        return render(request,'login/generate_fix_pdf.html',context={'company_id':company_id,'Delivery_No':Delivery_No,'Delivery_Term':Delivery_Term,'product_list':product_list,'customer_info':customer_info,'Invoice_date':Invoice_date,'Delivery_date':Delivery_date,'Invoice_no':Invoice_no,'Note':Note})
    else:
        return render(request, 'login/TpRepairOut.html',context={'TpFixdatabase': TpFixdatabase, 'Customerdatabase': Customerdatabase})

def generatePDF_fix_tr(request):
    TrFixdatabase = fix_tr_report.objects.all()
    Customerdatabase = customer.objects.all()
    if request.method == "POST":
        company_id = request.POST.get('company_id')
        product_id = request.POST.getlist("check")
        customerid = request.POST.get('customer')
        Invoice_date = request.POST.get('Invoicedate')
        Delivery_date = request.POST.get('Deliverydate')
        Invoice_no = request.POST.get('invoice_no')
        Note = request.POST.get('Note')
        Delivery_No = request.POST.get('DeliveryNo')
        Delivery_Term = request.POST.get('DeliveryTerm')
        customer_info = customer.objects.filter(customer_id=customerid).values()
        product_list = fix_tr_report.objects.filter(id__in=product_id).values()
        return render(request,'login/generate_fix_pdf.html',context={'company_id':company_id,'Delivery_No':Delivery_No,'Delivery_Term':Delivery_Term,'product_list':product_list,'customer_info':customer_info,'Invoice_date':Invoice_date,'Delivery_date':Delivery_date,'Invoice_no':Invoice_no,'Note':Note})
    else:
        return render(request, 'login/TrRepairOut.html',context={'TrFixdatabase': TrFixdatabase, 'Customerdatabase': Customerdatabase})