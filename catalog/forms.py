from django import forms
from .models import *

class AddPostForm(forms.Form):
    order_sum = forms.IntegerField(label="Сумма заказа")
    customer_id = forms.ModelChoiceField(queryset=Customer.objects.all(), label="Заказщик", empty_label="Заказщик не выбран")

class AddСustomerForm(forms.Form):
    customer_name = forms.CharField(max_length = 200, label='Название заказщика')
