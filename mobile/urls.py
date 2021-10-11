from django.urls import path
from mobile.views import index,create_brand,list_brand,update_brand,delete_brand,create_product,list_product,edit_product,view_product,delete_product

urlpatterns=[
    path("home",index,name="home"),
    path("brands",create_brand,name="createbrand"),
    path("brandlist",list_brand,name="brandlist"),
    path("brands/<int:id>",update_brand,name="update"),
    path("brands/remove/<int:id>",delete_brand,name="deletebrand"),
    path("products",create_product,name="createproduct"),
    path("mobilelist",list_product,name="mobilelist"),
    path("change/<int:id>",edit_product,name="updateproduct"),
    path("view/<int:id>",view_product,name="viewproduct"),
    path("remove/<int:id>",delete_product,name="deleteproduct"),

]