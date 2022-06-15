from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .froms import UserForm, AddNewProduct, Modify_fix, Modify_Product, addNewCustomer, addRepairProduct
from . import models
from .models import Trproduct, Tproduct, Prproduct, fix_tr_report, fix_tp_report,customer
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from datetime import datetime



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
    edit_form_fix = Modify_fix(request.GET)
    return render(request,'login/index.html',context={'Trdatabase': Trdatabase ,'Tdatabase':Tdatabase,'Prdatabase':Prdatabase,'FixTrDatabase':FixTrDatabase,'FixTpDatabase':FixTpDatabase,'edit_form_fix':edit_form_fix})

def add_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('Product_id')
        product_name = request.POST.get('Product_name')
        Product_no = request.POST.get('Product_no')
        Product_Price = request.POST.get('Product_Price')
        Product_time = request.POST.get('Product_time')
        company = request.POST.get('Product_Company')
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

def modify_fix_product(request,id):
    if request.method == 'POST':
        product_record = request.POST.get('fixed_Record')
        product_state = request.POST.get('Fixed_State')
        if  product_record == '' or product_state == '':
            return render(request, 'login/add.html', {'ret': 'error!'})
        models.fix_tr_report.objects.filter(id=id).update(fix_state = product_record, fixed_detail = product_state)
        models.fix_tp_report.objects.filter(id=id).update(fix_state = product_record, fixed_detail = product_state)
        return redirect('/index/')
    else:
        return render(request, '/index/',locals())

def TrSubpage(request):
    return render(request,'login/TRsubpage.html',locals())

def TrProductList(request):
    modify_form = Modify_Product()
    Trdatabase = Trproduct.objects.all()
    return render(request,'login/TRproductList.html',context={'Trdatabase':Trdatabase,'modify_form':modify_form})


def TrProductStockOut(request):
    Trdatabase = Trproduct.objects.all()
    Customerdatabase = customer.objects.all()

        #generatePDF(request,custom_info )
        #return redirect('/generate_pdf/', {'custom_info': custom_info})
    return render(request, 'login/TRproductOut.html',context={'Trdatabase': Trdatabase,'Customerdatabase':Customerdatabase})

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
    if request.method == 'POST':
        fix_id = request.POST.get('fix_id')
        fix_product_id = request.POST.get('fix_product_id')
        fix_product_name = request.POST.get('fix_product_name')
        fix_product_description = request.POST.get('fix_product_description')
        fix_state = request.POST.get('fix_state')
        fix_detail = request.POST.get('fix_detail')
        company = request.POST.get('Product_Company')
        if fix_id == '' or fix_product_id =='' or fix_product_name=='' or fix_product_description=='' or fix_state=='' or fix_detail=='':
            return render(request,'login/addnewproduct.html',{'ret':'error!'})
        if company == 'fix_tr_report':
            models.fix_tr_report.objects.create(fixed_id=fix_id, tr_product_id=fix_product_id,
                                            tr_product_name=fix_product_name, tr_product_description=fix_product_description,
                                            fix_state=fix_state,fixed_detail=fix_detail)
            message = "add successful!"
        elif company == 'fix_tp_report':
                models.fix_tp_report.objects.create(fixed_id=fix_id, tp_product_id=fix_product_id,
                                                    tp_product_name=fix_product_name,
                                                    tp_product_description=fix_product_description,
                                                    fix_state=fix_state, fixed_detail=fix_detail)
                message = "add successful!"
        else:
            message = "error!"
    repair_form = addRepairProduct()
    return render(request, 'login/addrepairproduct.html', locals())

def addnewcustomer(request):
    customer_form = addNewCustomer()
    return render(request,'login/addnewcustomer.html',locals())

def generatePDF(request):
    Trdatabase = Trproduct.objects.all()
    Customerdatabase = customer.objects.all().values()
    if request.method == "POST":
        product_id = request.POST.getlist("check")
        product_quantity = list(filter(None,request.POST.getlist('quantity')))
        customerid = request.POST.get('customer')
        Invoice_date = request.POST.get('Invoicedate')
        Delivery_date = request.POST.get('Deliverydate')
        Invoice_no = request.POST.get('invoice_no')
        Note = request.POST.get('Note')
        customer_info = customer.objects.filter(customer_id=customerid).values()
        product_list = Trproduct.objects.filter(id__in=product_id).values()
        print(product_quantity)
        return render(request,'login/generate_pdf.html',context={'product_list':product_list,'product_quantity':product_quantity,'customer_info':customer_info,'Invoice_date':Invoice_date,'Delivery_date':Delivery_date,'Invoice_no':Invoice_no,'Note':Note})
    else:
        return render(request, 'login/TRproductOut.html',
                      context={'Trdatabase': Trdatabase, 'Customerdatabase': Customerdatabase})
