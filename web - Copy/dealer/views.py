import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from pip._internal.network import auth
from django.contrib.auth import authenticate
from django.contrib import auth
from django.db import connection
from django.http import FileResponse
import io
from io import BytesIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import uuid
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from .models import Dealer
from .forms import DealerForm, UsernLoginForm
from customer.models import General_Item_Order, Medicinal_Item_Order
from customer.forms import GeneralItemOrderForm, MedicinalItemOrderForm


# Create your views here.
def shown(request):
    dealers = Dealer.objects.all()
    return render(request, "shown.html", {'dealers': dealers})


def deal(request):
    if request.method == "POST":
        status = 0
        form = DealerForm(request.POST)
        lic = request.POST['lic']
        shop = request.POST['shop']
        dealer = str(request.POST['dealer'])
        owner = str(request.POST['owner'])
        city = str(request.POST['city'])
        contact = (request.POST['contact'])
        if shop.isdigit():
            messages.info(request, "Shop Name cant be digit,Dealer Registration Failed,Try Again")
            return redirect('/deal')
        elif dealer.isdigit():
            messages.info(request, "Dealer type cant be digit,Dealer Registration Failed,Try Again")
            return redirect('/deal')
        elif owner.isdigit():
            messages.info(request, "Owner type cant be digit,Dealer Registration Failed,Try Again")
            return redirect('/deal')
        elif city.isdigit():
            messages.info(request, "City cant be digit,Dealer Registration Failed,Try Again")
            return redirect('/deal')
        elif not contact.isdigit():
            messages.info(request, "Phone number must be digits,Dealer Registration Failed,Try Again")
            return redirect('/deal')
        else:
            if form.is_valid():
                try:
                    deal1 = Dealer.objects.all()
                    for d in deal1:
                        if d.lic == lic:
                            status = 1
                            break

                    if status == 0:
                        form.save()
                        messages.success(request, "Dealer Registered")
                        return redirect('/deal')
                    else:
                        pass
                except:
                    return redirect('/deal')

            else:
                messages.error(request, 'License number already exist')
                return redirect('/deal')

    else:
        form = DealerForm()
        # messages.error(request, 'Dealer Not Registered')
        return render(request, 'registern.html', {'form': form})


def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        utype = request.POST['ut']

        status = 0
        user = Dealer.objects.all()
        for dealer in user:
            if dealer.username == username and dealer.password == password:
                status = 1
                break

        if status == 1:
            user5 = Dealer.objects.get(username=username)
            rlic = user5.lic
            if utype == 'general':
                qry = "SELECT * from general_item_order WHERE deal_id = %s"
                lic5 = General_Item_Order.objects.raw(qry, [rlic])
                return render(request, 'homen.html', {'user5': user5, 'lic5': lic5})
            else:
                qry = "SELECT * from medicinal_item_order WHERE deal_id = %s"
                lic2 = Medicinal_Item_Order.objects.raw(qry, [rlic])
                return render(request, 'med_home.html', {'user5': user5, 'lic2': lic2})

        else:
            messages.error(request, "Incorrect Credentials,Try again logging in")
            return redirect("/loginn")
    return render(request, "loginn.html")


def med_home(request):
    return render(request, "med_home.html")


def homen(request):
    return render(request, "homen.html")


def editn(request, lic):
    dealer = Dealer.objects.get(lic=lic)
    return render(request, 'editn.html', {'dealer': dealer})


def updaten(request, lic):
    dealer = Dealer.objects.get(lic=lic)
    form = DealerForm(request.POST, instance=dealer)
    if form.is_valid():
        form.save()
        return redirect("/shown")
    return render(request, 'editn.html', {'dealer': dealer})


def view(request, lic):
    dealer = Dealer.objects.get(lic=lic)
    return render(request, 'view.html', {'dealer': dealer})


def destroyn(request, lic):
    dealer = Dealer.objects.get(lic=lic)
    dealer.delete()
    return redirect("/shown")


def testn(request):
    lic5 = General_Item_Order.objects.all()
    return render(request, 'homen.html', {'lic5': lic5})


def tests(request):
    lic2 = Medicinal_Item_Order.objects.all()
    return render(request, 'med_home.html', {'lic2': lic2})


def bill(request, order_no):
    bills = General_Item_Order.objects.get(order_no=order_no)
    amt = bills.price * bills.qty
    with connection.cursor() as cursor:
        cursor.execute("UPDATE general_item_order SET bill_amount=%s WHERE order_no=%s",
                       [amt, bills.order_no])
    ##qry = "select * from general_item_order where deal_id=%s"
    ##lic5 = General_Item_Order.objects.raw(qry, bills.deal_id)
    ##return redirect(request, 'bill.html', {'lic5': lic5})
    # qry = "SELECT * from general_item_order WHERE order_no=order_no"
    order = General_Item_Order.objects.get(order_no=order_no)
    deal = Dealer.objects.get(lic=order.deal_id)
    return render(request, 'bill.html', {'order': order, 'deal': deal})


def supply(request, order_no):
    item = General_Item_Order.objects.get(order_no=order_no)
    rlic = item.deal_id
    with connection.cursor() as cursor:
        cursor.execute("UPDATE general_item_order SET status='Supplied' WHERE order_no=%s",
                       [item.order_no])
    qry = "SELECT * from general_item_order WHERE deal_id = %s"
    lic5 = General_Item_Order.objects.raw(qry, [rlic])
    # return render(request, 'homen.html', {'user5': user5, 'lic5': lic5})
    # lic5 = General_Item_Order.objects.all()
    return render(request, 'homen.html', {'lic5': lic5})



def supplys(request, order_no):
    med = Medicinal_Item_Order.objects.get(order_no=order_no)
    rlic = med.deal_id
    with connection.cursor() as cursor:
        cursor.execute("UPDATE medicinal_item_order SET allot_status='Supplied' WHERE order_no=%s",
                       [med.order_no])
    qry = "SELECT * from medicinal_item_order WHERE deal_id = %s"
    lic2 = Medicinal_Item_Order.objects.raw(qry, [rlic])
    # return render(request, 'homen.html', {'user5': user5, 'lic5': lic5})
    # lic5 = General_Item_Order.objects.all()
    return render(request, 'med_home.html', {'lic2': lic2})

# generate pdf
def bill_pdf(request, order_no):
    bills = General_Item_Order.objects.get(order_no=order_no)
    deal = Dealer.objects.get(lic=bills.deal_id)
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 30)
    dname = "                    " + str(deal.shop)
    wave = "_  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  "
    waves = "-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -"

    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 20)
    phone = "PHONE NUMBER             :" + str(deal.contact)
    email = "EMAIL                                :" + str(deal.email)
    ono = "ORDER NUMBER             :" + str(bills.order_no)
    textobs = c.beginText()
    textobs.setTextOrigin(inch, inch)
    textobs.setFont("Helvetica", 10)
    product = "PRODUCT NAME               :" + str(bills.name)
    qty = "PRODUCT QUANTITY       :" + str(bills.qty)
    price = "PRODUCT PRICE              :" + str(bills.price)
    total = "GRAND TOTAL                  :" + str(bills.bill_amount)

    heads = [
        dname,
        wave,
        waves,
        "",
        "",
        "",
        "",
    ]
    for head in heads:
        textobj.textLine(head)
    c.drawText(textobj)

    lines = [
        "",
        "",
        "",
        "",
        "",
        phone,
        email,
        ono,
        wave,
        waves,

    ]
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)

    txt = [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        product,
        qty,
        price,
        total,
        "",
        waves,
        wave,
        'THANK YOU HAPPY SHOPPING ,STAY HOME STAY SAFE ',
    ]
    for t in txt:
        textobs.textLine(t)
        c.drawText(textobs)

    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='bill.pdf')
