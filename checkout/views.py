from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QyMP8RxTyE2XC4yNzgskx6P2wOBDQ8EBCMWlq8xl98lx3RPx8vxcleq1HecN4FDyf7fdxt7NVMC6hogONhRZ2Jv00whs1ofXG',
        'client_secret': 'test',
    }

    return render(request, template, context)
