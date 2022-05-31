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

class Tproduct(models.Model):
    tp_product = models.CharField(max_length=256)
    tr_product = models.CharField(max_length=256)
    pr_product = models.CharField(max_length=256)

class Trproduct(models.Model):
    tr_product = models.CharField(max_length=256)
    tr_product_name = models.CharField(max_length=256)
    tr_product_description = models.CharField(max_length=256)


class Prproduct(models.Model):
    pr_product = models.CharField(max_length=256)
    pr_product_name = models.CharField(max_length=256)
    pr_product_description = models.CharField(max_length=256)



