from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("signup_view",views.signup_view,name="signup_view"),
    path("auth",views.auth,name="auth"),
    path("login_view",views.login_view,name="login_view"),
    path("login",views.login_confirm,name="login"),
    path("logout",views.logout_view,name="logout_view"),
    path("addcart",views.addcart,name="addcart"),
    path("cart",views.cart,name="cart"),
    path("delItem",views.deleteItem,name="deleteItem"),
]
