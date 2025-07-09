from django.shortcuts import redirect
from products.models import Product

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    if not isinstance(cart, dict):
        cart = {}

    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    request.session['cart'] = cart
    return redirect('view_cart')

def clear_cart(request):
    request.session['cart'] = {}
    return redirect('view_cart')

def update_quantity(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        quantity = int(request.POST.get('quantity', 1))
        cart[str(product_id)] = quantity
        request.session['cart'] = cart
    return redirect('view_cart')