from django.urls import path
from e_commerce import views

urlpatterns = [
    path('product_inventory/', views.product_inventory_view, name='product_inventory'),
    path('product_list/', views.product_list_view, name='product_list')
]