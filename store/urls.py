from django.urls import path
from .views import store, product

urlpatterns = [
    path('', store, name='store'),
    path('product/', product, name='product'),
]