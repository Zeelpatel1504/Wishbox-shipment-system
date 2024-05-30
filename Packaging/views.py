from django.shortcuts import render
from django.http import request

# Create your views here.
def home(request):
    return render(request, "home-5.html")

def priceTable(request, id):
     return render(request, "price-table-packaging.html", {"id" : id})