from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login ,logout


# Create your views here.
@login_required(login_url='login.html')
def dashboard(request):
    return render(request,'dashboard.html')

def index(request):
    return render(request,'index.html')

@login_required(login_url='login.html')
def display_customers(request):
    items=Farmers.objects.all()

    context={
        'items': items,
        'header':'customer',
    }

    return render(request,'customers.html',context)

@login_required(login_url='login.html')
def display_products(request):
    items=Product.objects.all()

    context={
        'items': items,
        'header':'product',
    }

    return render(request,'products.html',context)

@login_required(login_url='login.html')
def display_payments(request):
    items=Payments.objects.all()

    context={
        'items': items,
        'header':'payment',
    }

    return render(request,'payments.html',context)


def display_login(request):
    return render(request,'login.html')

@login_required(login_url='login.html')
def add_customer(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_customers')
    else:
        form=CustomerForm()
        return render(request,'item_entry.html',{'form':form})

@login_required(login_url='login.html')
def add_product(request):
    if request.method=="POST":
        form=ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_products')
    else:
        form=ProductForm()
        return render(request,'item_entry.html',{'form':form})

@login_required(login_url='login.html')
def add_payment(request):
    if request.method=="POST":
        form=PaymentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_payment')
    else:
        form=PaymentForm()
        return render(request,'item_entry.html',{'form':form})


def user_auth_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        
        return redirect('dashboard')
    else:
        return redirect('display_login')


def user_auth_logout(request):
    logout(request)
    return redirect('index')


def edit_customer(request,pk):
    item = get_object_or_404(Farmers,pk=pk)

    if request.method == "POST":
        form=CustomerForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_customers')
    else:
        form=CustomerForm(instance=item)

        return render(request,'edit_item.html',{'form':form})


def edit_product(request,pk):
    item = get_object_or_404(Product,pk=pk)

    if request.method == "POST":
        form=ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_products')
    else:
        form=ProductForm(instance=item)

        return render(request,'edit_item.html',{'form':form})


def edit_payment(request,pk):
    item = get_object_or_404(Payments,pk=pk)

    if request.method == "POST":
        form=PaymentForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_payments')
    else:
        form=PaymentForm(instance=item)

        return render(request,'edit_item.html',{'form':form})

def delete_customer(request,pk):
    Farmers.objects.filter(farmerID=pk).delete()
    items=Farmerst
    .objects.all()
   
    return redirect('display_customers')


def delete_product(request,pk):
    Product.objects.filter(productID=pk).delete()
    items=Product.objects.all()
    return redirect('display_products')


def delete_payment(request,pk):
    Payments.objects.filter(paymentID=pk).delete()
    items=Payments.objects.all()
    return redirect('display_payments')

