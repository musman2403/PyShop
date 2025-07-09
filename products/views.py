from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Product

def index(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    return render(request, 'index.html', {'products': products, 'cart': cart})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id not in cart:
        cart.append(product_id)
    request.session['cart'] = cart
    return redirect('view_cart')

from django.shortcuts import render, redirect
from products.models import Product

def view_cart(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    # Calculate total
    total_price = 0
    for product in products:
        quantity = int(cart.get(str(product.id), 1))
        total_price += product.price * quantity

    return render(request, 'cart.html', {
        'products': products,
        'cart': cart,
        'total_price': total_price
    })



def new(request):
    return HttpResponse('New products')


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
