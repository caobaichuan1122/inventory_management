from django import forms
from django.forms import NumberInput, Textarea


class UserForm(forms.Form):
    username = forms.CharField(label="user", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="password", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class AddNewProduct(forms.Form):
    company_name=[('Trproduct','Toprail Services'),('Tproduct','T-Power'),('Prproduct','Pranstek')]
    Product_id = forms.CharField(label="Product Code", max_length=256,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    Product_name = forms.CharField(label="Product Name", max_length=256,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    Product_no = forms.IntegerField(label="Product Number", help_text="Enter Number",
                                    widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Product_Price = forms.DecimalField(label="Product Price ($AU) ", max_digits=2, help_text="Enter Number",
                                       widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Product_time = forms.DateTimeField(label="Time",
                                       widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}))
    Product_Company = forms.ChoiceField(choices=company_name, widget=forms.Select(attrs={'class': 'form-control'}))


class Modify_fix(forms.Form):
    Fixed_State = forms.CharField(label="Fixed State", max_length=256,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    fixed_Record = forms.CharField(label="Fixed Record", max_length=256,
                                   widget=forms.Textarea(attrs={'class': 'form-control'}))


class Modify_Product(forms.Form):
    Product_id = forms.CharField(label="Product Code", max_length=256,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    Product_name = forms.CharField(label="Product Name", max_length=256,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    Product_num = forms.IntegerField(label="Product Number", help_text="Enter Number",
                                     widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Product_Price = forms.DecimalField(label="Product Price ($AU) ", max_digits=2, help_text="Enter Number",
                                       widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Product_time = forms.DateTimeField(label="Time",
                                       widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}))


class addRepairProduct(forms.Form):
    company_name=[('Trproduct','Toprail Services'),('Tproduct','T-Power'),('Prproduct','Pranstek')]
    fix_id = forms.CharField(label="Fixed Code", max_length=256,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    fix_product_id = forms.CharField(label="Fixed Product Code", max_length=256,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    fix_product_name = forms.CharField(label="Product Name", max_length=256,
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    fix_product_description = forms.CharField(label="Product Description", max_length=256,
                                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    fix_state = forms.CharField(label="Fixed State", max_length=256,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    fix_detail = forms.CharField(label="Fixed Record", max_length=256,
                                 widget=forms.Textarea(attrs={'class': 'form-control'}))
    Product_Company = forms.ChoiceField(choices=company_name, widget=forms.Select(attrs={'class': 'form-control'}))


class addNewCustomer(forms.Form):
    customer_id = forms.CharField(label="Customer ID", max_length=256,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_name = forms.CharField(label="Customer Name", max_length=256,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_phone = forms.CharField(label="Customer Phone Number", max_length=256,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_address = forms.CharField(label="Customer Address", max_length=256,
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_email = forms.CharField(label="Customer Email", max_length=256,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_type = forms.CharField(label="Customer Type", max_length=256,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
