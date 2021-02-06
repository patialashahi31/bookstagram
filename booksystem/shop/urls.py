from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("index2", views.index2, name="index2"),
    path("about/", views.about, name="AboutUs"),
    path("knowus/", views.knowus, name="KnowUs"),
    path("backhome/", views.backhome, name="backhome"),
    path("contact/", views.contact, name="ContactUs"),
    path("contact2/", views.contact2, name="Contact"),
    path("contact3/", views.contact3, name="Contact"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("products2/<int:myid>", views.productView2, name="ProductView2"),
    path("checkout/", views.checkout, name="Checkout"),
    path("insert/",views.insert,name='insert'),
    path("loginpage/",views.loginpage,name='loginpage'),
    path("logincheck/",views.logincheck,name='logincheck'),
    path("books/",views.books,name='books'),
]
