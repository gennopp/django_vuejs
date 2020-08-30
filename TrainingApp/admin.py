from django.contrib import admin

from .models import Dish, Restaurant, Order

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(Order)
