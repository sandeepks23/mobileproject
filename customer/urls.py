from django.urls import path
from customer.views import register,sign_in,sign_out,index,user_home,item_detail,add_to_cart,view_cart,del_from_cart,place_order,view_orders,cancel_order

urlpatterns=[
    path("createcustomer",register,name="register"),
    path("login",sign_in,name="login"),
    path("logout",sign_out,name="logout"),
    path("index",index,name="index"),
    path("home",user_home,name="home"),
    path("item/<int:id>",item_detail,name="items"),
    path("carts/<int:id>",add_to_cart,name="addtocarts"),
    path("viewcart",view_cart,name="viewcart"),
    path("removeitem/<int:id>",del_from_cart,name="removeitem"),
    path("placeorder/<int:id>/<int:cid>",place_order,name="placeorder"),
    path("vieworders",view_orders,name="vieworders"),
    path("removeorder/<int:id>",cancel_order,name="removeorder")

]