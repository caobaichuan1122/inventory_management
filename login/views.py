from .froms import UserForm, AddNewProduct, Modify_fix, Modify_Product, addNewCustomer, addRepairProduct
from .models import Trproduct, Tproduct, Prproduct, fix_tr_report, fix_tp_report,customer
from django.shortcuts import render,redirect
from .froms import UserForm,AddNewProduct,Modify_fix,Modify_Product
from . import models
from .models import Trproduct, Tproduct, Prproduct, fix_tr_report, fix_tp_report




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
    # hiddle the completed
    FixTrDatabase = fix_tr_report.objects.filter().exclude(fix_state='completed').all()
    FixTpDatabase = fix_tp_report.objects.filter().exclude(fix_state='completed').all()
    # get tr data
    tr_que = Trproduct.objects.values_list('tr_product_num', flat=True)
    tr_que = list(map(float,tr_que))
    tr_price = Trproduct.objects.values_list('tr_product_price', flat=True)
    tr_price = list(map(float,tr_price))
    # get tp data
    tp_que = Tproduct.objects.values_list('tp_product_num', flat=True)
    tp_que = list(map(float,tp_que))
    tp_price = Tproduct.objects.values_list('tp_product_price', flat=True)
    tp_price = list(map(float,tp_price))
    # get pr data
    pr_que = Prproduct.objects.values_list('pr_product_num', flat=True)
    pr_que = list(map(float,pr_que))
    pr_price = Prproduct.objects.values_list('pr_product_price', flat=True)
    pr_price = list(map(float,pr_price))
    # calulate the total price
    sum_tr = sum([x * y for x, y in zip(tr_que,tr_price)])
    sum_tp = sum([x * y for x, y in zip(tp_que, tp_price)])
    sum_pr = sum([x * y for x, y in zip(pr_que, pr_price)])
    edit_form_fix = Modify_fix()
    return render(request,'login/index.html',context={'FixTrDatabase':FixTrDatabase,'FixTpDatabase':FixTpDatabase,
                                                      'sum_tr':sum_tr,'sum_tp':sum_tp,'sum_pr':sum_pr,'edit_form_fix':edit_form_fix})


def add_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('Product_id')
        product_name = request.POST.get('Product_name')
        Product_no = request.POST.get('Product_no')
        Product_Price = request.POST.get('Product_Price')
        Product_Cost = request.POST.get('Product_Cost')
        Product_time = request.POST.get('Product_time')
        company = request.POST.get('Product_Company')
        if product_id == '' or product_name =='' or Product_no=='' or Product_Price=='' or Product_time=='' or Product_Cost=='':
            return render(request,'login/addnewproduct.html',{'ret':'error!'})
        if company == 'Trproduct':
            models.Trproduct.objects.create(tr_product_id=product_id, tr_product_name=product_name,
                                            tr_product_num=Product_no, tr_product_price=Product_Price,
                                            tr_product_cost=Product_Cost,tr_product_time=Product_time)
            message = "add successful!"
        elif company == 'Tproduct':
            models.Tproduct.objects.create(tp_product_id=product_id, tp_product_name=product_name,
                                           tp_product_num=Product_no, tp_product_price=Product_Price,
                                           tp_product_cost=Product_Cost,tp_product_time=Product_time)
            message = "add successful!"
        elif company == 'Prproduct':
            models.Prproduct.objects.create(pr_product_id=product_id, pr_product_name=product_name,
                                            pr_product_num=Product_no, pr_product_price=Product_Price,
                                            pr_product_cost=Product_Cost,pr_product_time=Product_time)
            message = "add successful!"
        else:
            message = "error!"
    product_form = AddNewProduct()
    return render(request,'login/addnewproduct.html',locals())

def del_fix_product(request,id):
    models.fix_tr_report.objects.filter(id=id).delete()
    models.fix_tp_report.objects.filter(id=id).delete()
    return redirect('/index/')

def del_product(request,id):
    models.Tproduct.objects.filter(id=id).delete()
    models.Trproduct.objects.filter(id=id).delete()
    models.Prproduct.objects.filter(id=id).delete()
    return redirect('/TrProductList/')

def modify_fix_product(request,id):
    if request.method == 'POST':
        product_record = request.POST.get('fixed_Record')
        product_state = request.POST.get('Fixed_State')
        models.fix_tr_report.objects.filter(id=id).update(fix_state = product_state, fixed_detail = product_record)
        models.fix_tp_report.objects.filter(id=id).update(fix_state = product_state, fixed_detail = product_record)
        return redirect('/index/')
    else:
        return render(request, '/index/',locals())

def modify_fix_list_product(request,id):
    if request.method == 'POST':
        product_record = request.POST.get('fixed_Record')
        product_state = request.POST.get('Fixed_State')
        models.fix_tr_report.objects.filter(id=id).update(fix_state = product_state, fixed_detail = product_record)
        models.fix_tp_report.objects.filter(id=id).update(fix_state = product_state, fixed_detail = product_record)
        return redirect('/repair_list/')
    else:
        return render(request, '/repair_list/',locals())

def modify_fix_tr_product(request,id):
    if request.method == 'POST':
        product_record = request.POST.get('fixed_Record')
        product_state = request.POST.get('Fixed_State')
        models.fix_tr_report.objects.filter(id=id).update(fix_state = product_state, fixed_detail = product_record)
        return redirect('/TrRepairList/')
    else:
        return render(request, '/TrRepairList/',locals())

def modify_fix_tp_product(request,id):
    if request.method == 'POST':
        product_record = request.POST.get('fixed_Record')
        product_state = request.POST.get('Fixed_State')
        models.fix_tp_report.objects.filter(id=id).update(fix_state = product_state, fixed_detail = product_record)
        return redirect('/TpRepairList/')
    else:
        return render(request, '/TpRepairList/',locals())

def modify_tr_product(request,id):
    if request.method == 'POST':
        product_id = request.POST.get('Product_id')
        product_name = request.POST.get('Product_name')
        Product_num = request.POST.get('Product_num')
        Product_Price = request.POST.get('Product_Price')
        Product_Cost = request.POST.get('Product_Cost')
        Product_time = request.POST.get('Product_time')
        models.Trproduct.objects.filter(id=id).update(tr_product_id = product_id, tr_product_name = product_name,
                                                      tr_product_num = Product_num, tr_product_price = Product_Price,
                                                      tr_product_cost = Product_Cost, tr_product_time = Product_time)
        return redirect('/TrProductList/')
    else:
        return render(request, '/TrProductList/',locals())

def modify_tp_product(request,id):
    if request.method == 'POST':
        product_id = request.POST.get('Product_id')
        product_name = request.POST.get('Product_name')
        Product_num = request.POST.get('Product_num')
        Product_Price = request.POST.get('Product_Price')
        Product_Cost = request.POST.get('Product_Cost')
        Product_time = request.POST.get('Product_time')
        models.Tproduct.objects.filter(id=id).update(tp_product_id = product_id, tp_product_name = product_name,
                                                     tp_product_num = Product_num, tp_product_price = Product_Price,
                                                     tp_product_cost = Product_Cost, tp_product_time = Product_time)
        return redirect('/TpProductList/')
    else:
        return render(request, '/TpProductList/',locals())

def modify_pr_product(request,id):
    if request.method == 'POST':
        product_id = request.POST.get('Product_id')
        product_name = request.POST.get('Product_name')
        Product_num = request.POST.get('Product_num')
        Product_Price = request.POST.get('Product_Price')
        Product_Cost = request.POST.get('Product_Cost')
        Product_time = request.POST.get('Product_time')
        models.Prproduct.objects.filter(id=id).update(pr_product_id = product_id, pr_product_name = product_name,
                                                      pr_product_num = Product_num, pr_product_price = Product_Price,
                                                      pr_product_cost = Product_Cost, pr_product_time = Product_time)
        return redirect('/PrProductList/')
    else:
        return render(request, '/PrProductList/',locals())

def del_fix_product(request,id):
    models.fix_tr_report.objects.filter(id=id).delete()
    models.fix_tp_report.objects.filter(id=id).delete()
    return redirect('/index/')

def TrSubpage(request):
    return render(request,'login/TRsubpage.html',locals())

def TpSubpage(request):
    return render(request,'login/TPsubpage.html',locals())

def PrSubpage(request):
    return render(request,'login/PRsubpage.html',locals())

def TrProductList(request):
    modify_form = Modify_Product()
    Trdatabase = Trproduct.objects.all()
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
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        customer_name = request.POST.get('customer_name')
        customer_phone = request.POST.get('customer_phone')
        customer_address = request.POST.get('customer_address')
        customer_email = request.POST.get('customer_email')
        customer_type = request.POST.get('customer_type')
        if customer_id == '' or customer_name =='' or customer_phone=='' or customer_address=='' or customer_email=='' or customer_type=='':
            return render(request,'login/addnewcustomer.html',{'ret':'error!'})

        models.customer.objects.create(customer_id=customer_id, customer_name=customer_name,
                                       customer_phone=customer_phone, customer_address=customer_address,
                                       customer_email=customer_email,customer_type=customer_type)
        message = "add successful!"
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
        return render(request,'login/generate_pdf.html',context={'product_list':product_list,
                                                                 'product_quantity':product_quantity,
                                                                 'customer_info':customer_info,
                                                                 'Invoice_date':Invoice_date,
                                                                 'Delivery_date':Delivery_date,
                                                                 'Invoice_no':Invoice_no,
                                                                 'Note':Note})
    else:
        return render(request, 'login/TRproductOut.html',
                      context={'Trdatabase': Trdatabase, 'Customerdatabase': Customerdatabase})

def completed(request,id):
    models.fix_tr_report.objects.filter(id=id).update(fix_state = 'Completed')
    models.fix_tp_report.objects.filter(id=id).update(fix_state = 'Completed')
    return redirect('/index/')

def list_completed(request,id):
    models.fix_tr_report.objects.filter(id=id).update(fix_state = 'Completed')
    models.fix_tp_report.objects.filter(id=id).update(fix_state = 'Completed')
    return redirect('/repair_list/')

def tr_completed(request,id):
    models.fix_tr_report.objects.filter(id=id).update(fix_state = 'Completed')
    return redirect('/TrRepairList/')

def tp_completed(request,id):
    models.fix_tp_report.objects.filter(id=id).update(fix_state = 'Completed')
    return redirect('/TpRepairList/')

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
        return render(request,'login/generate_pdf.html',context={'company_id':company_id,'Delivery_No':Delivery_No,'Delivery_Term':Delivery_Term,
                                                                 'product_list':product_list,'product_quantity':product_quantity,'customer_info':customer_info,
                                                                 'Invoice_date':Invoice_date,'Delivery_date':Delivery_date,'Invoice_no':Invoice_no,'Note':Note,'sum_quantity':sum_quantity})
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
        return render(request,'login/generate_pdf.html',context={'company_id':company_id,'Delivery_No':Delivery_No,
                                                                 'Delivery_Term':Delivery_Term,'product_list':product_list,
                                                                 'product_quantity':product_quantity,'customer_info':customer_info,
                                                                 'Invoice_date':Invoice_date,'Delivery_date':Delivery_date,
                                                                 'Invoice_no':Invoice_no,'Note':Note,'sum_quantity':sum_quantity})
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
        return render(request,'login/generate_pdf.html',context={'company_id':company_id,'Delivery_No':Delivery_No,
                                                                 'Delivery_Term':Delivery_Term,'product_list':product_list,
                                                                 'product_quantity':product_quantity,'customer_info':customer_info,
                                                                 'Invoice_date':Invoice_date,'Delivery_date':Delivery_date,
                                                                 'Invoice_no':Invoice_no,'Note':Note,'sum_quantity':sum_quantity})
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
        return render(request,'login/generate_fix_pdf.html',context={'company_id':company_id,'Delivery_No':Delivery_No,
                                                                     'Delivery_Term':Delivery_Term,'product_list':product_list,
                                                                     'customer_info':customer_info,'Invoice_date':Invoice_date,
                                                                     'Delivery_date':Delivery_date,'Invoice_no':Invoice_no,
                                                                     'Note':Note})
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
        return render(request,'login/generate_fix_pdf.html',context={'company_id':company_id,'Delivery_No':Delivery_No,
                                                                     'Delivery_Term':Delivery_Term,'product_list':product_list,
                                                                     'customer_info':customer_info,'Invoice_date':Invoice_date,
                                                                     'Delivery_date':Delivery_date,'Invoice_no':Invoice_no,
                                                                     'Note':Note})
    else:
        return render(request, 'login/TrRepairOut.html',context={'TrFixdatabase': TrFixdatabase, 'Customerdatabase': Customerdatabase})

def TrProductStockOut(request):
    Trdatabase = Trproduct.objects.all()
    Customerdatabase = customer.objects.all()
    return render(request, 'login/TRproductOut.html',
                  context={'Trdatabase': Trdatabase, 'Customerdatabase': Customerdatabase})

def TpProductStockOut(request):
    Tpdatabase = Tproduct.objects.all()
    Customerdatabase = customer.objects.all()
    return render(request, 'login/TPproductOut.html',
                  context={'Tpdatabase': Tpdatabase, 'Customerdatabase': Customerdatabase})

def TpRepairStockOut(request):
    TpFixdatabase = fix_tp_report.objects.all()
    Customerdatabase = customer.objects.all()
    return render(request, 'login/TpRepairOut.html',
                  context={'TpFixdatabase': TpFixdatabase, 'Customerdatabase': Customerdatabase})

def TrRepairStockOut(request):
    TrFixdatabase = fix_tr_report.objects.all()
    Customerdatabase = customer.objects.all()
    return render(request, 'login/TrRepairOut.html',
                  context={'TrFixdatabase': TrFixdatabase, 'Customerdatabase': Customerdatabase})

def PrProductStockOut(request):
    Prdatabase = Prproduct.objects.all()
    Customerdatabase = customer.objects.all()
    return render(request, 'login/PRproductOut.html',
                  context={'Prdatabase': Prdatabase, 'Customerdatabase': Customerdatabase})

def please_login(request):
    return render(request,'login/pleaselogin.html')


def add_product_quantity(request):
    id = request.POST.get("AddProduct")
    id_list_tr = Trproduct.objects.values_list('tr_product_id', flat=True)
    id_list_tp = Tproduct.objects.values_list('tp_product_id', flat=True)
    id_list_pr = Prproduct.objects.values_list('pr_product_id', flat=True)
    if request.method == "POST":
        if id in id_list_tr:
            quantity = models.Trproduct.objects.filter(tr_product_id=id).values('tr_product_num')
            models.Trproduct.objects.filter(tr_product_id=id).update(tr_product_num = quantity[0]["tr_product_num"] + 1)
        elif id in id_list_tp:
            quantity = models.Tproduct.objects.filter(tp_product_id=id).values('tp_product_num')
            models.Tproduct.objects.filter(tp_product_id=id).update(tp_product_num = quantity[0]["tp_product_num"] + 1)
        elif id in id_list_pr:
            quantity = models.Prproduct.objects.filter(pr_product_id=id).values('pr_product_num')
            models.Prproduct.objects.filter(pr_product_id=id).update(pr_product_num = quantity[0]["pr_product_num"] + 1)
        else:
            print(123)
            message = "ID does not exist, please re-enter!"
            render(request, 'login/Add_products.html')
    return render(request,'login/Add_products.html')

def invoicePDF(request):
    return render(request,'login/InvoicePDF.html')

def QuotePDF(request):
    return render(request,'login/QuotePDF.html')

def tr_order(request):
    return render(request,'login/tr_order_list.html')


