from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'Kitmain/home_index.html')

def products(request):
    return render(request,'Kitmain/product_index.html')