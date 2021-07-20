from django.shortcuts import render

def sklep(request):
    context = {}
    return render(request, 'magazyn/sklep.html', context)

def cart(request):
    context = {}
    return render(request, 'magazyn/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'magazyn/checkout.html', context)
# Create your views here.
