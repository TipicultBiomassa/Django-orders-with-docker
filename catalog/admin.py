from django.contrib import admin

# Register your models here.

from .models import Order, Customer


admin.site.register(Order)
admin.site.register(Customer)




