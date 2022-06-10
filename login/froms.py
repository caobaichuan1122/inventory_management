from django import forms
from django.forms import NumberInput,Textarea


class UserForm(forms.Form):
    username = forms.CharField(label="user", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class AddNewProduct(forms.Form):
    company_name=[('Trproduct','Toprail Services'),('Tproduct','T-Power'),('Prproduct','Pranstek')]
    Product_id = forms.CharField(label="Product Code", max_length=256, widget=forms.TextInput(attrs={'class':'form-control'}))
    Product_name = forms.CharField(label="Product Name", max_length=256, widget=forms.TextInput(attrs={'class':'form-control'}))
    Product_no = forms.IntegerField(label="Product quantity",help_text="Enter Number",widget=forms.NumberInput(attrs={'class':'form-control'}))
    Product_Price = forms.DecimalField(label="Product Price ($AU) ",max_digits=2,help_text="Enter Number",widget=forms.NumberInput(attrs={'class':'form-control'}))
    Product_time = forms.DateTimeField(label="Date",widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type':'date'}))
    Product_Company = forms.ChoiceField(choices=company_name,widget=forms.Select(attrs={'class':'form-control'}))

class Modify_fix(forms.Form):
    Fixed_State = forms.CharField(label="Fixed State", max_length=256, widget=forms.TextInput(attrs={'class':'form-control'}))
    fixed_Record = forms.CharField(label="Fixed Record", max_length=256, widget=forms.Textarea(attrs={'class':'form-control'}))

class Modify_Product(forms.Form):
    Product_id = forms.CharField(label="Product Code",max_length=256,widget=forms.TextInput(attrs={'class':'form-control'}))
    Product_name = forms.CharField(label="Product Name",max_length=256,widget=forms.TextInput(attrs={'class':'form-control'}))
    Product_num = forms.IntegerField(label="Product Number",help_text="Enter Number",widget=forms.NumberInput(attrs={'class':'form-control'}))
    Product_Price = forms.DecimalField(label="Product Price ($AU) ", max_digits=2, help_text="Enter Number",widget=forms.NumberInput(attrs={'class':'form-control'}))
    Product_time = forms.DateTimeField(label="Time",widget=forms.DateTimeInput(attrs={'class':'form-control', 'type':'date'}))
