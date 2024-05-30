from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home-4.html", {"id":3})

def priceTable(request, id):
     return render(request, "price-table-sea.html", {"id" : id})