from django.shortcuts import render,redirect

# Create your views here.

from customer.forms import CustomerCreate,LoginForm
from django.contrib.auth import authenticate,login,logout

from mobile.models import Product,Cart,Orders
from customer.decorators import login_required,permission_required,remove_order_permission
from customer.forms import PlaceOrderForm
from django.db.models import Sum

def register(request,*args,**kwargs):
    form=CustomerCreate()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=CustomerCreate(request.POST)
        form.save()
        return redirect("login")
    else:
        context["form"]=form
        return render(request, "register.html", context)
    return render(request,"register.html",context)

def sign_in(request,*args,**kwargs):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("home")
        else:
            print("invalid")
    return render(request,"login.html",context)

def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("login")

def index(request):
    return render(request,"index.html")

@login_required
def user_home(request,*args,**kwargs):
    cnt=Cart.objects.filter(user=request.user,status="ordernotplaced").count()

    mobiles=Product.objects.all()
    context={
        "mobiles":mobiles,
        "cnt":cnt
    }
    return render(request,"home.html",context)

def cart_count(user):
    cnt = Cart.objects.filter(user=user, status="ordernotplaced").count()
    return cnt

@login_required
def item_detail(request,*args,**kwargs):
    id=kwargs.get("id")
    mobile=Product.objects.get(id=id)
    context={
        "mobile":mobile,
        "cnt":cart_count(request.user)
    }

    return render(request,"productdetails.html",context)


@login_required
def add_to_cart(request,*args,**kwargs):
    id=kwargs.get("id")
    product=Product.objects.get(id=id)
    cart=Cart(product=product,user=request.user)
    cart.save()
    return redirect("viewcart")

@login_required
def view_cart(request,*args,**kwargs):
    cart_items=Cart.objects.filter(user=request.user,status="ordernotplaced")
    total = Cart.objects.filter(status="ordernotplaced", user=request.user).aggregate(Sum('product__price'))

    context={
        "cart_items":cart_items,
        "total":total.get('product__price__sum'),
        "cnt": cart_count(request.user)
    }
    return render(request,"mycart.html",context)


@login_required
@permission_required
def del_from_cart(requst,*args,**kwargs):
    id=kwargs.get("id")
    cart_item=Cart.objects.get(id=id)
    cart_item.delete()
    return redirect("viewcart")

@login_required
def place_order(request,*args,**kwargs):
    id=kwargs.get("id")
    mobile=Product.objects.get(id=id)
    instance={
        "product":mobile.mobile_name
    }
    form=PlaceOrderForm(initial=instance)
    context={}
    context["form"]=form

    if request.method=="POST":
        cid=kwargs.get("cid")
        cart=Cart.objects.get(id=cid)

        form=PlaceOrderForm(request.POST)
        if form.is_valid():
            address=form.cleaned_data.get("address")
            product=mobile
            order=Orders(address=address,product=product,user=request.user)
            order.save()
            cart.status="orderplaced"
            cart.save()
            return redirect("home")

    return render(request,"placeorder.html",context)

@login_required
def view_orders(request,*args,**kwargs):
    orders=Orders.objects.filter(user=request.user,status="ordered")

    context={
        "orders":orders,
        "cnt": cart_count(request.user)
    }
    # context["orders"]=orders
    return render(request,"vieworders.html",context)


@login_required
@remove_order_permission
def cancel_order(request,*args,**kwargs):
    id=kwargs.get("id")
    order=Orders.objects.get(id=id)
    order.status="cancelled"
    order.save()
    return redirect("vieworders")





