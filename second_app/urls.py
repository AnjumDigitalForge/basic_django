from django.urls import path
from second_app import views


urlpatterns = [
    path('products/', views.product, name='product_list'),
]