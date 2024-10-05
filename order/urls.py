from django.urls import path
from .views import order_content, order_complete


urlpatterns = [
    path('', order_content, name='order_content'),
    path('complete/', order_complete, name='order_complete')
]