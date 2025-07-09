from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<int:product_id>/', views.update_quantity, name='update_quantity'),
    path('clear/', views.clear_cart, name='clear_cart'),
]
