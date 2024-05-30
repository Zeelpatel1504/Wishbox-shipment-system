from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="pack-home",),
    path('price-table/<int:id>', priceTable, name="price-table"),

]