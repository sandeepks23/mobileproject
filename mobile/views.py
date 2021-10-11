from django.shortcuts import render,redirect
from mobile.forms import BrandForm,ProductForm
from mobile.models import Brand,Product

# Create your views here.

def index(request):
    return render(request,"home.html")


def create_brand(request):
    forms=BrandForm()
    context={}
    context["forms"]=forms
    if request.method=="POST":
        forms=BrandForm(request.POST)
        if forms.is_valid():
            brandname=forms.cleaned_data.get("brand_name")
            brand=Brand(brand_name=brandname)
            brand.save()
            return render(request,"index.html")
    return render(request,"addbrands.html",context)

def list_brand(request):
    brands=Brand.objects.all()
    context={}
    context["brands"]=brands
    return render(request,"brandlist.html",context)

def update_brand(request,id):
    brand=Brand.objects.get(id=id)
    instance={
        "brand_name":brand.brand_name
    }
    form=BrandForm(initial=instance)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BrandForm(request.POST)
        if form.is_valid():
            brandname=form.cleaned_data.get("brand_name")
            brand.brand_name=brandname
            brand.save()
            return redirect("brandlist")
    return render(request,"updatebrand.html",context)

def delete_brand(request,id):
    brand=Brand.objects.get(id=id)
    brand.delete()
    return redirect("brandlist")

def create_product(request):
    form=ProductForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ProductForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("mobilelist")
        else:
            context["form"]=form
            return render(request,"createproduct.html",context)
    return render(request,"createproduct.html",context)



def list_product(request):
    mobiles=Product.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobilelist.html",context)


def get_object(id):
    return Product.objects.get(id=id)

def edit_product(request,*args,**kwargs):
    id=kwargs.get("id")
    product=get_object(id)
    form=ProductForm(instance=product)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ProductForm(instance=product,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("mobilelist")
    return render(request,"editmobile.html",context)


def view_product(request,*args,**kwargs):
    id=kwargs.get("id")
    product=get_object(id)
    context={}
    context["product"]=product
    return render(request,"viewmobile.html",context)

def delete_product(request,*args,**kwargs):
    id=kwargs.get("id")
    product=get_object(id)
    product.delete()
    return redirect("mobilelist")