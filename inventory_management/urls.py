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
    path('generate_pdf/', views.generatePDF, name="generate_pdf"),
    path('generate_pdftp/', views.generatePDF_tp, name="generate_pdftp"),
    path('generatePDF_pr/', views.generatePDF_pr, name="generate_pdfpr"),
    path('generate_fix_pdftp/', views.generatePDF_fix_tp, name="generate_fix_pdftp"),
    path('generate_fix_pdftr/', views.generatePDF_fix_tr, name="generate_fix_pdftr"),
    path('TrProductStockOut/', views.TrProductStockOut, name='TrProductStockOut'),
    path('TpProductStockOut/', views.TpProductStockOut, name='TpProductStockOut'),
    path('PrProductStockOut/', views.PrProductStockOut, name='PrProductStockOut'),
    path('TpRepairStockOut/', views.TpRepairStockOut, name="TpRepairStockOut"),
    path('TrRepairStockOut/', views.TrRepairStockOut, name="TrRepairStockOut"),
    path('please_login/',views.please_login,name="please_login"),
    path('add_product_quantity/',views.add_product_quantity,name="add_product_quantity"),
    path('invoicePDF_tp/<int:id>',views.invoicePDF_tp,name="invoicePDF_tp"),
    path('invoicePDF_tr/<int:id>',views.invoicePDF_tr,name="invoicePDF_tr"),
    path('invoicePDF_pr/<int:id>',views.invoicePDF_pr,name="invoicePDF_pr"),
    path('QuotePDF_tp/<int:id>',views.QuotePDF_tp,name="QuotePDF_tp"),
    path('QuotePDF_tr/<int:id>',views.QuotePDF_tr,name="QuotePDF_tr"),
    path('QuotePDF_pr/<int:id>',views.QuotePDF_pr,name="QuotePDF_pr"),
    path('tr_order/', views.tr_order, name="tr_order"),
    path('tp_order/', views.tp_order, name="tp_order"),
    path('pr_order/', views.pr_order, name="pr_order"),
    path('repair_edit/<int:id>',views.repair_record_edit,name="repair_edit"),
    path('repair_edit_tp/<int:id>',views.repair_record_edit_tp,name="repair_edit_tp"),
    path('repair_tr_report/<int:id>',views.repair_tr_report,name="repair_tr_report"),
    path('repair_tp_report/<int:id>',views.repair_tp_report,name="repair_tp_report"),
    path('delivery_note_tr/<int:id>',views.delivery_note_tr,name="delivery_note_tr"),
    path('delivery_note_tp/<int:id>',views.delivery_note_tp,name="delivery_note_tp"),
    path('delivery_note_pr/<int:id>',views.delivery_note_pr,name="delivery_note_pr"),
    # path('sum/',views.sum,name="sum"),
]
