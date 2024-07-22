from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')
def craft(request):
    return render(request, 'main/craft.html')
def delivery(request):
    return render(request, 'main/delivery.html')
def info(request):
    return render(request, 'main/info.html')
def cart(request):
    return render(request, 'main/cart.html')
