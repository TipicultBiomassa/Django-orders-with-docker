from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('addpage/', views.addpage, name='add_page'),
    path('addcustomer/', views.addcustomer, name='add_customer'),
    path('json/', views.json, name='json'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.order_delete, name='order_delete')
    #path('<int:article_id>/', views.detail, name = 'detail')
]



