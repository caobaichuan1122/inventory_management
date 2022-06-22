"""inventory_management URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_pdfkit import PDFView
from wkhtmltopdf.views import PDFTemplateView
from login import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('add_product/', views.add_product, name='add_product'),
    path('del_fix_tr_product/<int:id>', views.del_fix_tr_product, name='del_fix_tr_product'),
    path('del_fix_tp_product/<int:id>', views.del_fix_tp_product, name='del_fix_tp_product'),
    path('modify_fix_product/<int:id>',views.modify_fix_product,name='modify_fix_product'),
    path('TrSubpage/', views.TrSubpage, name='TrSubpage'),
    path('TpSubpage/', views.TpSubpage, name='TpSubpage'),
    path('PrSubpage/', views.PrSubpage, name='PrSubpage'),
    path('TrProductList/', views.TrProductList, name='TrProductList'),
    path('TrProductStockOut/', views.TrProductStockOut, name='TrProductStockOut'),
    path('TpProductStockOut/', views.TpProductStockOut, name='TpProductStockOut'),
    path('PrProductStockOut/', views.PrProductStockOut, name='PrProductStockOut'),
    path('add_repair_product/',views.addrepairproduct,name="add_repair_product"),
    path('add_new_customer/',views.addnewcustomer,name='add_new_customer'),
    path('generate_pdf/',views.generatePDF,name="generate_pdf"),
    path('generate_pdftp/', views.generatePDF_tp, name="generate_pdftp"),
    path('generate_pdfpr/', views.generatePDF_pr, name="generate_pdfpr"),
    path('TpProductList/',views.TpProductList,name="TpProductList"),
    path('PrProductList/',views.PrProductList,name="PrProductList"),
    path('TotalRepairList/',views.repair_list,name="TotalRepairList"),
    path('TprepairList/',views.TpRepairList,name="TprepairList"),
    path('TrrepairList/', views.TrRepairList, name="TrrepairList"),
    path('TpRepairStockOut/',views.TpRepairStockOut, name="TpRepairStockOut"),
    path('TrRepairStockOut/',views.TrRepairStockOut, name="TrRepairStockOut"),
    path('generate_fix_pdftp/',views.generatePDF_fix_tp,name="generate_fix_pdftp"),
    path('generate_fix_pdftr/',views.generatePDF_fix_tr,name="generate_fix_pdftr")
    #path('generate_fix_pdftp/', PDFTemplateView.as_view(template_name='login/generate_fix_pdf.html',filename='deliverynote.pdf'), name='my-pdf')

]
