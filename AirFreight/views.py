from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from Wishbox import settings
from RoadFreight.models import *

# Create your views here.
def home(request):
    return render(request, "home-3.html", {"id":2})

def priceTable(request, id):
     return render(request, "price-table-air.html", {"id" : id})