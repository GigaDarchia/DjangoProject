from django.urls import path
from .views import store, product, categories, products

urlpatterns = [
    path('', store, name='store'),
    path('product/', product, name='product'),
    path('categories/', categories, name='categories'),
    path('products/', products, name='products')
]