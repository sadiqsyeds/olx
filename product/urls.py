from django.urls import path
from . import views

app_name = 'product'


urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.productlist, name='product_list'),
    path('<str:slug>',views.productdetails, name='product_detail')
]