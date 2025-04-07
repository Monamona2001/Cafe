from django.urls import path
from. import views
urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="AboutUs"),
    path("menu/", views.menu, name="Menu"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="tracking"),
    path("search/", views.search, name="Search"),
     path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="checkout"),
]