from django.urls import path
from . import views
urlpatterns = [
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('check_cart/', views.check_cart, name='check_cart'),
    path('check_cart/delete_cart/<int:id>/', views.delete_cart, name='delete_cart')
]
