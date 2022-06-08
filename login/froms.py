from django import forms
from django.forms import NumberInput


class UserForm(forms.Form):
    username = forms.CharField(label="user", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class AddNewProduct(forms.Form):
    company_name=[('login_trproduct','Toprail Services'),('login_tproduct','T-Power'),('login_prproduct','Pranstek')]
    Product_id = forms.CharField(label="Product Code", max_length=256, widget=forms.TextInput(attrs={'class':'form-control'}))
    Product_name = forms.CharField(label="Product Name", max_length=256, widget=forms.TextInput(attrs={'class':'form-control'}))
    Product_no = forms.IntegerField(label="Product Number",help_text="Enter Number",widget=forms.NumberInput(attrs={'class':'form-control'}))
    Product_Price = forms.DecimalField(label="Product Price ($AU) ",max_digits=2,help_text="Enter Number",widget=forms.NumberInput(attrs={'class':'form-control'}))
    Product_time = forms.DateTimeField(label="Time",widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type':'date'}))
    Product_Company = forms.ChoiceField(choices=company_name,widget=forms.Select(attrs={'class':'form-control'}))