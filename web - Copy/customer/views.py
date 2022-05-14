from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from customer import views
from django.db import connection
from .models import Customer, Complaint_Registration, Feedback, Product, General_Item_Order, Medicinal_Item_Order, \
    General_Item_Order
from .forms import CustomerForm, UsersLoginForm, ComplaintRegistrationForm, FeedbackForm, MedicinalItemOrderForm, \
    GeneralItemOrderForm


def logins(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        status = 0
        user = Customer.objects.all()
        for customer in user:
            if customer.username == username and customer.password == password:
                status = 1
                break

        if status == 1:
            return redirect("/homes")
        else:
            messages.info(request, "Incorrect Credentials,Try again logging in")
            return redirect("/logins")
    return render(request, "logins.html")


def cust(request):
    if request.method == "POST":
        status = 0
        form = CustomerForm(request.POST)
        id = request.POST['id']
        name = request.POST['name']
        city = str(request.POST['city'])
        contact = (request.POST['contact'])
        if name.isdigit():
            messages.info(request, "Customer Name cant be digit,Customer Registration Failed,Try Again")
            return redirect('/cust')
        elif city.isdigit():
            messages.info(request, "City cant be digit,Customer Registration Failed,Try Again")
            return redirect('/cust')
        elif not contact.isdigit():
            messages.info(request, "Phone number must be digits,Customer Registration Failed,Try Again")
            return redirect('/cust')
        else:
            if form.is_valid():
                try:
                    cust1 = Customer.objects.all()
                    for c in cust1:
                        if c.id == id:
                            status = 1
                            break

                    if status == 0:
                        form.save()
                        return redirect('/logins')
                    else:
                        pass
                except:
                    return redirect('/cust')

            else:
                messages.error(request, 'Customer id already exist')
                return redirect('/cust')

    else:
        form = CustomerForm()
        # messages.error(request, 'Customer Not Registered')
        return render(request, 'registers.html', {'form': form})


def shows(request):
    customers = Customer.objects.all()
    return render(request, "shows.html", {'customers': customers})


def homes(request):
    return render(request, "homes.html")


def next(request):
    return render(request, "Next.html")


def productfetch(request):
    products = Product.objects.all()
    # order = request.POST['order_no']
    # order_n = General_Item_Order.objects.get(order_no=order)
    return render(request, "productfetch.html", {'products': products})


def general_item_order(request):
    if request.method == "POST":
        saverecord = General_Item_Order()
        saverecord.order_no = request.POST['order_no']
        saverecord.id = request.POST['id']
        saverecord.name = request.POST['name']
        saverecord.pid = request.POST['pid']
        saverecord.price = request.POST['price']
        saverecord.order_date = request.POST['order_date']
        saverecord.qty = request.POST['qty']
        saverecord.save()
    product = Product.objects.all()
    return render(request, 'next.html', {'product': product})


def medicinal_order(request):
    if request.method == "POST":
        status = 0
        form = MedicinalItemOrderForm(request.POST)
        order_no = request.POST['order_no']
        med_name = str(request.POST['med_name'])
        manufacturer = str(request.POST['manufacturer'])
        scale = str(request.POST['scale'])
        if med_name.isdigit():
            messages.info(request, "Medicine Name cant be digit,Medicine order Failed,Try Again")
            return redirect('/medicinal_order')
        elif manufacturer.isdigit():
            messages.info(request, "manufacturer cant be digit,Medicine Order Failed,Try Again")
            return redirect('/medicinal_order')
        elif scale.isdigit():
            messages.info(request, "scale cant be only digit,must include mg,Medicine Order Failed,Try Again")
            return redirect('/medicinal_order')
        if form.is_valid():
            try:
                med1 = Medicinal_Item_Order.objects.all()
                for m in med1:
                    if m.order_no == order_no:
                        status = 1
                        break

                if status == 0:
                    form.save()
                    messages.success(request, 'Medicinal Order placed')
                    return redirect('/medicinal_order')
                else:
                    pass
            except:
                return redirect('/medicinal_order')

        else:
            messages.success(request, " Order number already exist")
            return redirect("/medicinal_order")

    else:
        form = MedicinalItemOrderForm()
        # messages.info(request, 'order Not placed')
        return render(request, 'medicinal_order.html', {'form': form})


def medicinal_order_detail(request):
    medicinal_orders = Medicinal_Item_Order.objects.all()
    return render(request, 'medicinal_order_detail.html', {'medicinal_orders': medicinal_orders})


def order_detail(request):
    item_orders = General_Item_Order.objects.all()
    return render(request, 'order_detail.html', {'item_orders': item_orders})


def complaint_registration(request):
    if request.method == "POST":
        status = 0
        form = ComplaintRegistrationForm(request.POST)
        comp_id = request.POST['comp_id']
        complaint = str(request.POST['complaint'])
        if complaint.isdigit():
            messages.info(request, "Complaint cant be digit,Complaint Registration Failed,Try Again")
            return redirect('/complaint_registration')

        else:
            if form.is_valid():
                try:
                    comp1 = Complaint_Registration.objects.all()
                    for c in comp1:
                        if c.comp_id == comp_id:
                            status = 1
                            break

                    if status == 0:
                        form.save()
                        messages.success(request, 'Complaint placed')
                        return redirect('/complaint_registration')
                    else:
                        pass
                except:
                    return redirect('/complaint_regsitration')
            else:
                messages.error(request, 'Complaint ID already exist')
                return redirect('/complaint_registration')

    else:
        form = ComplaintRegistrationForm()
        # messages.info(request, 'complaint Not placed')
        return render(request, 'complaint_registration.html', {'form': form})


def complaints(request):
    complaint_registrations = Complaint_Registration.objects.all()
    return render(request, 'complaints.html', {'complaint_registrations': complaint_registrations})


def feedback(request):
    if request.method == "POST":
        status = 0
        form = FeedbackForm(request.POST)
        feed_id = request.POST['feed_id']
        feed = str(request.POST['feed'])
        if feed.isdigit():
            messages.info(request, "Feedback cant be digit,Feedback Registration Failed,Try Again")
            return redirect('/feedback')
        else:
            if form.is_valid():
                try:
                    feed1 = Feedback.objects.all()
                    for f in feed1:
                        if f.feed_id == feed_id:
                            status = 1
                            break

                    if status == 0:
                        form.save()
                        messages.success(request, 'Feedback placed')
                        return redirect('/feedback')
                    else:
                        pass
                except:
                    return redirect('/feedback')
            else:
                messages.error(request, 'Feedback ID already exist')
                return redirect('/feedback')

    else:
        form = FeedbackForm()
        # messages.info(request, 'Feedback Not placed')
        return render(request, 'feedback.html', {'form': form})


def feedbacks(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedbacks.html', {'feedbacks': feedbacks})


def edits(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'edits.html', {'customer': customer})


def updates(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(request.POST, instance=customer)
    if form.is_valid():
        form.save()
        return redirect("/shows")
    return render(request, 'edits.html', {'customer': customer})


def destroys(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect("/shows")


def pload(request):
    products = Product.objects.all()
    return render(request, 'productfetch.html', {'products': products})


def cont(request):
    if request.method == "POST":
        pname = request.POST['name']
        prod = Product.objects.get(name=pname)
        return render(request, 'item_order.html', {'prod': prod})


def load(request):
    order = request.POST['order_no']
    order_n = General_Item_Order.objects.get(order_no=order)
    return render(request, 'item_order.html', {'order_n': order_n})


def view(request, comp_id):
    complaint = Complaint_Registration.objects.get(comp_id=comp_id)
    with connection.cursor() as cursor:
        cursor.execute("UPDATE complaint_registration SET status=True WHERE comp_id=%s",
                       [complaint.comp_id])
    return redirect("/complaints")
