from products.views import detailed_product_view, product_create_view, product_delete_view, product_list_view
from django.contrib import admin
from django.urls import path


app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('<int:id>', detailed_product_view, name='product_detail'),
    path('create/', product_create_view, name='product_create'),
    path('<int:id>/delete', product_delete_view, name='product_delete')
]
