from django.db import models


class User(models.Model):

    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    # email = models.EmailField(unique=True)
    # sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = 'user'
        verbose_name_plural = 'user'

class fix_tr_report(models.Model):
    fixed_id = models.CharField(max_length=256)
    tr_product_id = models.CharField(max_length=256)
    tr_product_name = models.CharField(max_length=256)
    tr_product_description = models.CharField(max_length=256)
    fix_state = models.CharField(max_length=256)
    fixed_detail = models.CharField(max_length=256)
    tr_product_fix_sn = models.CharField(max_length=256,default='xxx')


class fix_tp_report(models.Model):
    fixed_id = models.CharField(max_length=256)
    tp_product_id = models.CharField(max_length=256)
    tp_product_name = models.CharField(max_length=256)
    tp_product_description = models.CharField(max_length=256)
    fix_state = models.CharField(max_length=256)
    fixed_detail = models.CharField(max_length=256)
    tp_product_fix_sn = models.CharField(max_length=256,default='xxx')

# class Send_product(models.Model):
#     send_id = models.CharField(max_length=256)
#     product_id = models.CharField(max_length=256)
#     product_name = models.CharField(max_length=256)
#     product_num = models.CharField(max_length=256)
#     line_num = models.CharField(max_length=256)
#     product_price = models.CharField(max_length=256)
#
# class Send_product(models.Model):
#     send_id = models.CharField(max_length=256)
#     product_id = models.CharField(max_length=256)
#     product_name = models.CharField(max_length=256)
#     product_num = models.CharField(max_length=256)
#     line_num = models.CharField(max_length=256)
#     product_price = models.CharField(max_length=256)

class tr_order_list(models.Model):
    order_id = models.CharField(max_length=256)
    delivery_note = models.CharField(max_length=256)
    delivery_term = models.CharField(max_length=256)
    custormer = models.CharField(max_length=256)
    issue_date = models.DateField(max_length=6)
    due_date = models.DateField(max_length=6)
    invoice_number = models.CharField(max_length=256)
    GST = models.FloatField(default=0.1)

class tp_order_list(models.Model):
    order_id = models.CharField(max_length=256)
    delivery_note = models.CharField(max_length=256)
    delivery_term = models.CharField(max_length=256)
    custormer = models.CharField(max_length=256)
    issue_date = models.DateField(max_length=6)
    due_date = models.DateField(max_length=6)
    invoice_number = models.CharField(max_length=256)
    GST = models.FloatField(default=0.1)

class pr_order_list(models.Model):
    order_id = models.CharField(max_length=256)
    delivery_note = models.CharField(max_length=256)
    delivery_term = models.CharField(max_length=256)
    custormer = models.CharField(max_length=256)
    issue_date = models.DateField(max_length=6)
    due_date = models.DateField(max_length=6)
    invoice_number = models.CharField(max_length=256)
    GST = models.FloatField(default=0.1)

class Prproduct(models.Model):
    pr_product_id = models.CharField(max_length=256)
    pr_product_name = models.CharField(max_length=256)
    pr_product_cost = models.CharField(max_length=256,default='100')
    pr_product_price = models.CharField(max_length=256)
    pr_product_time = models.DateField(max_length=6)
    pr_product_sn = models.CharField(max_length=256,default='xxx')
    pr_product_state = models.CharField(max_length=256, default='stock')


class Tproduct(models.Model):
    tp_product_id = models.CharField(max_length=256)
    tp_product_name = models.CharField(max_length=256)
    tp_product_cost = models.CharField(max_length=256,default='100')
    tp_product_price = models.CharField(max_length=256)
    tp_product_time = models.DateField(max_length=6)
    tp_product_sn = models.CharField(max_length=256, default='xxx')
    tp_product_state = models.CharField(max_length=256, default='stock')

class Trproduct(models.Model):
    tr_product_id = models.CharField(max_length=256)
    tr_product_name = models.CharField(max_length=256)
    tr_product_cost = models.CharField(max_length=256,default='100')
    tr_product_price = models.CharField(max_length=256)
    tr_product_time = models.DateField(max_length=6)
    tr_product_sn = models.CharField(max_length=256, default='xxx')
    tr_product_state = models.CharField(max_length=256, default='stock')
    tr_order_list_fk = models.ForeignKey('tr_order_list', on_delete=models.CASCADE,null=True)

# class tr_product_sn(models.Model):
#     tr_product_sn = models.CharField(max_length=256,default='xxx')
#     tr_product_sn_fk = models.ForeignKey('Trproduct', on_delete=models.CASCADE, null=True)
#
# class tp_product_sn(models.Model):
#     tp_product_sn = models.CharField(max_length=256,default='xxx')
#     tp_product_sn_fk = models.ForeignKey('Tproduct', on_delete=models.CASCADE, null=True)
#
# class pr_product_sn(models.Model):
#     pr_product_sn = models.CharField(max_length=256,default='xxx')
#     pr_product_sn_fk = models.ForeignKey('Prproduct', on_delete=models.CASCADE, null=True)

class customer(models.Model):
    customer_id = models.CharField(max_length=256)
    customer_name = models.CharField(max_length=256)
    customer_phone = models.CharField(max_length=256)
    customer_address = models.CharField(max_length=256)
    customer_email = models.CharField(max_length=256)
    customer_type = models.CharField(max_length=256)





