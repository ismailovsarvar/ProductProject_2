from django.shortcuts import render, redirect, get_object_or_404

from app.forms import ProductModelForm, CustomerAddForm
from app.models import Product, Customer


# from django.urls import reverse_lazy
# from django.views.generic import ListView, UpdateView, DeleteView


# Create your views here.

def index(request):
    products = Product.objects.all().order_by('-id')
    context = {
        'products': products
    }
    return render(request, 'app/index.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    attributes = product.get_attributes()
    context = {
        'product': product,
        'attributes': attributes
    }
    return render(request, 'app/product-details.html', context)


# def add_product(request):
#     form = ProductForm()
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         name = request.POST['name']
#         description = request.POST['description']
#         price = request.POST['price']
#         rating = request.POST['rating']
#         discount = request.POST['discount']
#         quantity = request.POST['quantity']
#         product = Product(name=name, description=description, price=price, rating=rating, discount=discount,
#                           quantity=quantity)
#         if form.is_valid():
#             product.save()
#             return redirect('index')
#
#     context = {
#         'form': form
#     }
#     return render(request, 'app/add-product.html', context)

def add_product(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'app/add-product.html', context)

