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
from login import views
from django_pdfkit import PDFView
# import pdfkit
# path_wkhtmltopdf = r'D:\wf\wkhtmltopdf\bin\wkhtmltopdf.exe'
# config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
# pdfkit.from_url("login/addnewproduct.html", "123.pdf", configuration=config)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add_product/', views.add_product, name='add_product'),
    path('del_fix_product/<int:id>', views.del_fix_product, name='del_fix_product'),
    path('del_product/<int:id>', views.del_product, name='del_product'),
    path('modify_fix_product/<int:id>',views.modify_fix_product,name='modify_fix_product'),
    path('TrSubpage/', views.TrSubpage, name='TrSubpage'),
    path('TpSubpage/', views.TpSubpage, name='TpSubpage'),
    path('PrSubpage/', views.PrSubpage, name='PrSubpage'),
    path('TrProductList/', views.TrProductList, name='TrProductList'),
    path('TpProductList/', views.TpProductList, name='TpProductList'),
    path('PrProductList/', views.PrProductList, name='PrProductList'),
    path('TrProductStockOut/', views.TrProductStockOut, name='TrProductStockOut'),
    path('addrepairproduct/',views.addrepairproduct,name="addrepairproduct"),
    path('addnewcustomer/',views.addnewcustomer,name='addnewcustomer'),
    path('generate_pdf/',views.generatePDF,name="generate_pdf"),
    path('completed/<int:id>',views.completed,name="completed"),
    path('repair_list/',views.repair_list,name="repair_list"),
    path('TpRepairList/',views.TpRepairList,name="TpRepairList"),
    path('TrRepairList/',views.TrRepairList,name="TrRepairList"),
    # path('mypdf/', PDFView.as_view( template_name = 'login/addnewproduct.html' ), name='mypdf'),


]
