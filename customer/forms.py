from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
class CustomerCreate(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password1":forms.PasswordInput(attrs={"class":"form-control"}),
            "password2":forms.PasswordInput(attrs={"class":"form-control"})
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))


class PlaceOrderForm(forms.Form):
    address=forms.CharField(widget=forms.Textarea(attrs={'class':"form-control"}))
    product=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
