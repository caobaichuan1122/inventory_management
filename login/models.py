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

class fix_tp_report(models.Model):
    fixed_id = models.CharField(max_length=256)
    tp_product_id = models.CharField(max_length=256)
    tp_product_name = models.CharField(max_length=256)
    tp_product_description = models.CharField(max_length=256)
    fix_state = models.CharField(max_length=256)
    fixed_detail = models.CharField(max_length=256)

class Prproduct(models.Model):
    pr_product_id = models.CharField(max_length=256)
    pr_product_name = models.CharField(max_length=256)
    pr_product_num = models.CharField(max_length=256)

class customer(models.Model):
    customer_id = models.CharField(max_length=256)
    customer_name = models.CharField(max_length=256)
    customer_phone = models.CharField(max_length=256)
    customer_address = models.CharField(max_length=256)
    customer_email = models.CharField(max_length=256)
    customer_type = models.CharField(max_length=256)

class Tproduct(models.Model):
    tp_product_id = models.CharField(max_length=256)
    tp_product_name = models.CharField(max_length=256)
    tp_product_num = models.CharField(max_length=256)

class Trproduct(models.Model):
    tr_product_id = models.CharField(max_length=256)
    tr_product_name = models.CharField(max_length=256)
    tr_product_num = models.CharField(max_length=256)



