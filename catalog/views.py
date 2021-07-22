from django.shortcuts import render

from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .forms import *
from .models import Order, Customer
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import json
from django.core import serializers
from django.http import HttpResponse
#from REST_FRAMEWORK.renderers import JSONRenderer

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    all_orders = Order.objects.order_by('-order_date')

    num_orders = Order.objects.all().count()
    num_customers = Customer.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_orders': num_orders, 'num_customers': num_customers,
                 'num_visits': num_visits, 'all_orders': all_orders},
    )


@login_required()
def json(request):
    data = serializers.serialize('json', Order.objects.all())
    response = HttpResponse(data, content_type='content_type/json')
    #response["Content-Disposition"] = 'attachment; filename=export.json'
    return response


@login_required()
def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST or None)
        if form.is_valid():
            #print(form.cleaned_data)
            Order.objects.create(**form.cleaned_data)
            return redirect('/catalog')
    else:
        form = AddPostForm()
    return render(request, './crud.html', {'form': form})
@login_required()
def addcustomer(request):
    if request.method == 'POST':
        #form1 = AddСustomerForm(request.POST)
        form1 = AddСustomerForm(request.POST)
        if form1.is_valid():
            Customer.objects.create(**form1.cleaned_data)
            return redirect('/catalog')
    else:
        form1 = AddСustomerForm()
    return render(request, './customeradd.html', {'form1': form1})

@login_required()
def order_delete(request, pk):
    cat = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        cat.delete()
        return redirect('/catalog')
    return render(request, 'index.html', {'order': order})


from django.views import generic



from django.contrib.auth.mixins import LoginRequiredMixin




# Added as part of challenge!
from django.contrib.auth.mixins import PermissionRequiredMixin



from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required, permission_required




