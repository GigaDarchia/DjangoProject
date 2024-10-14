from django.urls import path
from .views import store, categories_json, products_json, category, products, product

urlpatterns = [
    path('', store, name='store'),
    path('category/', category, name="category"),
    path('category/<int:category_id>/products/', products, name='category_products'),
    path('product/<int:product_id>/', product, name='product'),
    path('categories/', categories_json, name='categories'),
    path('products/', products_json, name='products')
]