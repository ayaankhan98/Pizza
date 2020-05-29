from django.contrib import admin
from .models import RegularPizza, SilicianPizza, Toppings, Subs, Extras, Pasta, Salads, DinnerPlatters,orders
# Register your models here.


admin.site.register(RegularPizza)
admin.site.register(SilicianPizza)
admin.site.register(Toppings)
admin.site.register(Subs)
admin.site.register(Extras)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(DinnerPlatters)
admin.site.register(orders)
