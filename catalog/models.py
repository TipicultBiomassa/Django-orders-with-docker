from django.db import models

# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns


from datetime import date

from django.contrib.auth.models import User




class Customer(models.Model):
    customer_name = models.CharField('Название заказщика', max_length = 200)
    customer_dateadded = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.customer_name

class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True, blank=True)
    order_sum = models.DecimalField(max_digits=50, decimal_places=2)

