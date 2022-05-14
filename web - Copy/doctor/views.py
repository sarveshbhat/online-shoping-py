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
from customer.models import Medicinal_Item_Order, General_Item_Order
from .models import Doctor
from .forms import DoctorForm
from customer.forms import MedicinalItemOrderForm


# username == null

# Create your views here.
def show(request):
    doctors = Doctor.objects.all()
    return render(request, "show.html", {'doctors': doctors})


def doc(request):
    if request.method == "POST":
        status = 0
        form = DoctorForm(request.POST)
        lic = request.POST['lic']
        name = str(request.POST['name'])
        spl = str(request.POST['specialist'])
        clinic = str(request.POST['clinic'])
        city = str(request.POST['city'])
        contact = (request.POST['contact'])
        if name.isdigit():
            messages.info(request, "Doctor Name cant be digit,Doctor Registration Failed,Try Again")
            return redirect('/doc')
        elif spl.isdigit():
            messages.info(request, "Specialization cant be digit,Doctor Registration Failed,Try Again")
            return redirect('/doc')
        elif clinic.isdigit():
            messages.info(request, "Clinic Name cant be digit,Doctor Registration Failed,Try Again")
            return redirect('/doc')
        elif city.isdigit():
            messages.info(request, "City cant be digit,Doctor Registration Failed,Try Again")
            return redirect('/doc')
        elif not contact.isdigit():
            messages.info(request, "Phone number must be digits,Doctor Registration Failed,Try Again")
            return redirect('/doc')
        else:
            if form.is_valid():
                try:
                    doc1 = Doctor.objects.all()
                    for d in doc1:
                        if d.lic == lic:
                            status = 1
                            break

                    if status == 0:
                        form.save()
                        messages.success(request, "Doctor Registered Successfully")
                        return redirect('/doc')
                    else:
                        pass
                except:
                    return redirect('/doc')
            else:
                messages.error(request, 'License number already exist')
                return redirect('/doc')

    else:
        form = DoctorForm()
        # messages.error(request, 'Doctor Not Registered')
        return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        status = 0
        user = Doctor.objects.all()
        for doctor in user:
            if doctor.username == username and doctor.password == password:
                status = 1
                break

        if status == 1:
            user1 = Doctor.objects.get(username=username)
            rlic = user1.lic
            qry = "SELECT * from medicinal_item_order WHERE lic = %s"
            lic1 = Medicinal_Item_Order.objects.raw(qry, [rlic])
            return render(request, 'home.html', {'user1': user1, 'lic1': lic1})
        else:
            messages.error(request, "Incorrect Credentials,Try again logging in")
            return redirect("/login_user")
    return render(request, "login.html")


def home(request):
    return render(request, "home.html")


def edit(request, lic):
    doctor = Doctor.objects.get(lic=lic)
    return render(request, 'edit.html', {'doctor': doctor})


def update(request, lic):
    doctor = Doctor.objects.get(lic=lic)
    form = DoctorForm(request.POST, instance=doctor)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'doctor': doctor})


def destroy(request, lic):
    doctor = Doctor.objects.get(lic=lic)
    doctor.delete()
    return redirect("/show")


def reject(request, order_no):
    medicinal_item_order = Medicinal_Item_Order.objects.get(order_no=order_no)
    qry = "SELECT * from medicinal_item_order WHERE lic = %s"
    lic1 = Medicinal_Item_Order.objects.raw(qry, [medicinal_item_order.lic])
    medicinal_item_order.delete()
    return render(request, 'home.html', {'lic1': lic1})


def test(request):
    lic3 = Medicinal_Item_Order.objects.all()
    return render(request, 'home.html', {'lic3': lic3})


def accept(request, order_no):
    medicine = Medicinal_Item_Order.objects.get(order_no=order_no)
    with connection.cursor() as cursor:
        cursor.execute("UPDATE medicinal_item_order SET status=True WHERE order_no=%s",
                       [medicine.order_no])
    #lic1 = Medicinal_Item_Order.objects.all()
    qry = "SELECT * from medicinal_item_order WHERE lic = %s"
    lic1 = Medicinal_Item_Order.objects.raw(qry, [medicine.lic])
    return render(request, 'home.html', {'lic1': lic1})
