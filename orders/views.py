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

## this view shows the index page of the webapp and the index page shows the
## resturant menu 
def index(request):
    ## context dictionary have all menu items of the resturant
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


## signup_view views just simply renders the signup page where
## users can create a new account
def signup_view(request):
    ## if a user is not already logged in only then render signup page 
    if not request.user.is_authenticated:
        return render(request,"orders/signup.html")
    ## else redirect the user to the index page for browsing the Resturant Menu
    return HttpResponseRedirect(reverse("index"))


## when the user successfully submits the signup form then this view takes the
## information given by the user and creates a new user based on that information
def auth(request):
    username = request.POST["username"] ## getting the username from the form
    first_name = request.POST["first_name"] ## getting the first name of user
    last_name = request.POST["last_name"] ## getting the last name of user
    email = request.POST["email"] ## getting the email id
    password = request.POST["password"] ## getting the  password  of user
    cnf_password = request.POST["cnf_password"] ## again getting the password just for conformation
    if(password == cnf_password): ## checking if and only if both passwords are same 
        try:
            ## created a new user if passwords matched
            User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        except IntegrityError:
            ## else if a user with same username exist then return the user to the
            ## signup page again
            return render(request,"orders/signup.html",{'message':f'User with Username {username} alredy exist !'})
    ## if both the passwords do not matched then redirect the user to the signup page again
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