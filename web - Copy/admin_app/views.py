import math
from urllib import request

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from pip._internal.network import auth
from django.contrib.auth import authenticate
from django.contrib import auth
from django.db import connection
import customer
import dealer
from dealer.models import Dealer
from customer.models import Medicinal_Item_Order, General_Item_Order
from dealer.forms import DealerForm
from customer.forms import MedicinalItemOrderForm, GeneralItemOrderForm


# Create your views here.

def login_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if username == "admin" and password == "admin":
            return redirect("/home_admin")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("/login_admin")
    return render(request, "login_admin.html")


def allot(request):
    list = []
    i = 0
    gcount = 0
    dcount = 0
    acount = 0
    qry = "SELECT * from general_item_order WHERE status = 'No'"
    general = General_Item_Order.objects.raw(qry)
    qry1 = "SELECT *  FROM dealer WHERE dealer = 'general'"
    dealer = Dealer.objects.raw(qry1)
    for gen in general:
        gcount = gcount + 1
    print(gcount)
    for deal in dealer:
        list.insert(i, deal.lic)
        i = i + 1
        dcount = dcount + 1

    acount = math.ceil(gcount / dcount)
    p = 0
    count = 0
    for gen in general:
        if count == dcount:
            count = 0
            p = 0
        if count < dcount:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE general_item_order SET deal_id=%s, status='Yes' WHERE order_no=%s",
                               [list[p], gen.order_no])
        count = count + 1
        p = p + 1
        print(count)
        print(p)

    return redirect("/order_detail")


def home_admin(request):
    return render(request, "home_admin.html")

def allots(request):
    list = []
    i = 0
    gcount = 0
    dcount = 0
    acount = 0
    qry = "SELECT * from medicinal_item_order WHERE status = True"
    medicinal = Medicinal_Item_Order.objects.raw(qry)
    qry1 = "SELECT *  FROM dealer WHERE dealer = 'medicinal'"
    dealer = Dealer.objects.raw(qry1)
    for med in medicinal:
        gcount = gcount + 1
    print(gcount)
    for deal in dealer:
        list.insert(i, deal.lic)
        i = i + 1
        dcount = dcount + 1

    acount = math.ceil(gcount / dcount)
    p = 0
    count = 0
    for med in medicinal:
        if count == dcount:
            count = 0
            p = 0
        if count < dcount:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE medicinal_item_order SET deal_id=%s, allot_status='Yes' WHERE order_no=%s",
                               [list[p], med.order_no])
        count = count + 1
        p = p + 1
        print(count)
        print(p)

    return redirect("/medicinal_order_detail")
