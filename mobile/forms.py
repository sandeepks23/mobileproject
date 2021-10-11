from django import forms
from django.forms import ModelForm
from mobile.models import Product


class BrandForm(forms.Form):
    brand_name=forms.CharField()

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        widgets={
            "mobile_name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "specs":forms.Textarea(attrs={"class":"form-control"}),
        }

    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data.get("price")
        if price<500:
            msg="Invalid price"
            self.add_error("price",msg)
