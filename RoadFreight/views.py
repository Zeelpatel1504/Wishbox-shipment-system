from django.shortcuts import render, redirect
from RoadFreight.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, "home-1.html", {"id": 1})


def orders(request, id, pkg):
    # try:
    if request.method == "POST":
        address = request.POST.get("address")
        p_address = request.POST.get("pickup_address")
        d_address = request.POST.get("drop_address")
        p_date = request.POST.get("p_date")
        mile = int(request.POST.get("mile"))
        if id == 1:
            if pkg == 1:
                mile_total_price =  199
            elif pkg == 2:
                mile_total_price =  213
            elif pkg == 3:
                mile_total_price =  813
            elif pkg == 4:
                mile_total_price =  613
        elif id == 2:
            if pkg == 1 and mile <= 50:
                mile_total_price = 400
            elif pkg == 2 and mile >= 50 and mile <= 100:
                mile_total_price = 600
            elif pkg == 3 and mile >= 100 and mile <= 200:
                mile_total_price = 1500
            elif pkg == 4 and mile >= 200 and mile <= 400:
                mile_total_price = 3000
        elif id == 3:
            if pkg == 1 and mile <= 500:
                mile_total_price = 800
            elif pkg == 2 and mile >= 500 and mile <= 700:
                mile_total_price = 1500
            elif pkg == 3 and mile >= 900 and mile <= 1000:
                mile_total_price = 2500
            elif pkg == 4 and mile >= 1000 and mile <= 2000:
                mile_total_price = 4000
        
        # order instance
        order = Order.objects.create(
            user=request.user,
            miles=mile,
            address=address,
            price=mile_total_price,
            pickup_address=p_address,
            drop_address=d_address,
            pickup_at=p_date,
        )

        context = {"oid": order.oid, "key": settings.STRIPE_PUBLISHABLE_KEY}
        return render(request, "payment.html", context)
    # except Exception as e:
    #     print("Something wrong")
    return render(request, "order.html", {"id": id, "pkg": pkg})


# class PaymentView(TemplateView):
#     template_name = 'payment.html'

#     def get_context_data(self, **kwargs):  # new
#         context = super().get_context_data(**kwargs)
#         context['key'] = settings.STRIPE_PUBLISHABLE_KEY
#         return context


def orderPlaced(request):
    return render(request, "orderplaced.html", {})


def viewOrders(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    print("====>>>> orders : ", orders, type(orders))
    return render(request, "orders.html", {"orders": orders})


def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        psw = request.POST["password"]

        user = User.objects.create_user(username=name, email=email, password=psw)
        user.first_name = name
        user.save()
        messages.success(request, "User registered successfully.")
        return redirect("login")
    return render(request, "register.html", {})


def login(request):
    if request.method == "POST":
        name = request.POST["name"]
        psw = request.POST["password"]

        user = authenticate(username=name, password=psw)
        if user.is_authenticated:
            auth_login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("login")
    return render(request, "login.html", {})


def logout(request):
    auth_logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")


def contact_us(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        requirement = request.POST.get("requirement")

        ContactUs.objects.create(
            fname=fname,
            lname=lname,
            email=email,
            contact=contact,
            requirement=requirement,
        )
        return redirect("home")
    return render(request, "contact_us.html")


def get_quote(request):
    print(request)
    if request.method == "POST":
        fname = request.POST.get("fname")
        email = request.POST.get("email")
        address = request.POST.get("address")
        message = request.POST.get("message")

        GetQuote.objects.create(
            fname=fname, email=email, address=address, message=message
        )
        return redirect("home")
    # return render(request, 'contact_us.html')


def about_us(request):
    return render(request, "aboutus.html", {})


def priceTable(request, id):
    return render(request, "price-table-road.html", {"id": id})
