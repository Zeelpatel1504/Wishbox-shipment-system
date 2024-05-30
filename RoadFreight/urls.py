from django.contrib import admin
from django.urls import path, include
from RoadFreight.views import *

from django.contrib import admin
from django.urls import path, include
from RoadFreight.views import *

urlpatterns = [
    path('', home, name="home"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    # path("orders/<float:id>/", orders, name="orders"),
    path("orders/<int:id>/<int:pkg>/", orders, name="orders"),
    # path("payment/", PaymentView.as_view(), name='payment'),
    path('orderplaced', orderPlaced, name='orderplaced'),
    path('view_orders', viewOrders, name='viewOrders'),
    path('contact-us/', contact_us, name='contactUs'),
    path('get-quote/', get_quote, name='get-quote'),
    path('about-us/', about_us, name='aboutUs'),
    path('price-table/<int:id>', priceTable, name="price-table-road"),
]