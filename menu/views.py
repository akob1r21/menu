from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Foods,Order
from django.contrib.auth.decorators import login_required

def register_viev(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if username and password and password==password2:
            user=User.objects.create_user(username=username, password=password)
            user.set_password(password)
            return redirect('log')
        return render(request,'register.html')
    return render(request,'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('home')
            return render(request,'login.html')
    return render(request,'login.html') 

def logout_view(request):
    logout(request)
    return redirect('log')

@login_required(login_url='log')
def home(request):
    food = Foods.objects.all()
    search = request.POST.get('search')
    if search:
        food = Foods.objects.filter(name__icontains = search)
    return render(request,'home.html',{'food':food})


def my_order(request):
    if not request.user.is_authenticated:
        return redirect('log')
    
    orders = Order.objects.filter(user = request.user)

    return render(request, 'my_orders.html', {'orders': orders})


def order(request, id):
    if not request.user.is_authenticated:
        return redirect('log') 
    
    foods = Foods.objects.filter(id=id).first()
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        
        if phone_number and address:
            Order.objects.create(
                user=request.user,
                food=foods,
                phone_number=phone_number,
                address=address
            )
            return redirect('my_order')
        
    return render(request, 'order.html', {'food': foods})

