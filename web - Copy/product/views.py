from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from product import views
from .models import Product
from .forms import ProductForm


# Create your views here.


def product(request):
    if request.method == "POST":
        status = 0
        form = ProductForm(request.POST)
        pid = request.POST['pid']
        name = str(request.POST['name'])
        type = str(request.POST['type'])
        quality = request.POST['quality']
        if name.isdigit():
            messages.info(request, "Product Name cant be digit,Product Entry Failed,Try Again")
            return redirect('/product')
        elif type.isdigit():
            messages.info(request, "Product type cant be digit,Product Entry Failed,Try Again")
            return redirect('/product')
        elif not quality.isdigit():
            messages.info(request, "Product quality must be digit,Product Entry Failed,Try Again")
            return redirect('/product')
        else:
            if form.is_valid():
                try:
                    pro1 = Product.objects.all()
                    for p in pro1:
                        if p.pid == pid:
                            status = 1
                            break

                    if status == 0:
                        form.save()
                        return redirect('/product_detail')
                    else:
                        pass
                except:
                    return redirect('/product')
            else:
                messages.error(request, 'Product id already exist')
                return redirect('/product')

    else:
        form = ProductForm()
        #messages.info(request, 'Product Not Added')
        return render(request, 'product/product.html', {'form': form})


def product_detail(request):
    products = Product.objects.all()
    return render(request, 'product/product_detail.html', {'products': products})


def product_edit(request, pid):
    product = Product.objects.get(pid=pid)
    return render(request, 'product/productedit.html', {'product': product})


def product_update(request, pid):
    product = Product.objects.get(pid=pid)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect("/product_detail")
    return render(request, 'product/productedit.html', {'product': product})


def product_destroy(request, pid):
    product = Product.objects.get(pid=pid)
    product.delete()
    return redirect("/product_detail")

