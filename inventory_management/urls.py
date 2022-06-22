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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('add_product/', views.add_product, name='add_product'),
    path('addrepairproduct/', views.addrepairproduct, name="addrepairproduct"),
    path('addnewcustomer/', views.addnewcustomer, name='addnewcustomer'),
    path('del_fix_product/<int:id>', views.del_fix_product, name='del_fix_product'),
    path('del_product/<int:id>', views.del_product, name='del_product'),
    path('modify_fix_product/<int:id>',views.modify_fix_product,name='modify_fix_product'),
    path('modify_fix_list_product/<int:id>',views.modify_fix_list_product,name='modify_fix_list_product'),
    path('modify_fix_tr_product/<int:id>',views.modify_fix_tr_product,name='modify_fix_tr_product'),
    path('modify_fix_tp_product/<int:id>',views.modify_fix_tp_product,name='modify_fix_tp_product'),
    path('modify_tr_product/<int:id>',views.modify_tr_product,name='modify_tr_product'),
    path('modify_tp_product/<int:id>',views.modify_tp_product,name='modify_tp_product'),
    path('modify_pr_product/<int:id>',views.modify_pr_product,name='modify_pr_product'),
    path('TrSubpage/', views.TrSubpage, name='TrSubpage'),
    path('TpSubpage/', views.TpSubpage, name='TpSubpage'),
    path('PrSubpage/', views.PrSubpage, name='PrSubpage'),
    path('TrProductList/', views.TrProductList, name='TrProductList'),
    path('TpProductList/', views.TpProductList, name='TpProductList'),
    path('PrProductList/', views.PrProductList, name='PrProductList'),
    path('TrProductStockOut/', views.TrProductStockOut, name='TrProductStockOut'),
    path('generate_pdf/',views.generatePDF,name="generate_pdf"),
    path('completed/<int:id>',views.completed,name="completed"),
    path('tr_completed/<int:id>',views.tr_completed,name="tr_completed"),
    path('tp_completed/<int:id>',views.tp_completed,name="tp_completed"),
    path('list_completed/<int:id>',views.list_completed,name="list_completed"),
    path('repair_list/',views.repair_list,name="repair_list"),
    path('TpRepairList/',views.TpRepairList,name="TpRepairList"),
    path('TrRepairList/',views.TrRepairList,name="TrRepairList"),

]
