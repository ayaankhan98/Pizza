from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse, JsonResponse
from .models import RegularPizza,SilicianPizza,Toppings,Salads,Pasta,DinnerPlatters,Extras,Subs,orders
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect


# Create your views here.

def index(request):
    context = {
        'RegularPizzas':RegularPizza.objects.all(),
        'SilicianPizzas':SilicianPizza.objects.all(),
        'Toppings':Toppings.objects.all(),
        'Subs': Subs.objects.all(),
        'Pastas': Pasta.objects.all(),
        'Salads':Salads.objects.all(),
        'DinnerPlatters':DinnerPlatters.objects.all(),
        'Extras':Extras.objects.all(),

    }
    return render(request,"orders/index.html",context)


def signup_view(request):
    if not request.user.is_authenticated:
        return render(request,"orders/signup.html")
    return HttpResponseRedirect(reverse("index"))


def auth(request):
    username = request.POST["username"]
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    password = request.POST["password"]
    cnf_password = request.POST["cnf_password"]
    if(password == cnf_password):
        try:
            User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        except IntegrityError:
            return render(request,"orders/signup.html",{'message':f'User with Username {username} alredy exist !'})
    return HttpResponse("User Not Created")


def login_view(request):
    if not request.user.is_authenticated:
        return render(request,"orders/login.html",{'message':''})
    return HttpResponseRedirect(reverse("index"))


def login_confirm(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request,username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"orders/login.html",{'message':'Invalid Credentials'})
    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def addcart(request):
    if request.user.is_authenticated:
        item_class = request.POST["item_class"]
        item_name = request.POST["item_name"]
        size = request.POST.get('size',"None")
        quantity = request.POST["quantity"]
        new_order = orders(item=item_name,size=size,quantity=quantity,user=request.user.username)
        new_order.save()
        return JsonResponse({'status':True})
    return JsonResponse({'status':False})

def cart(request):
    return render(request,"orders/cart.html")