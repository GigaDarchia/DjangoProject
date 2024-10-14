from django.http import HttpResponse
from django.shortcuts import render
def order_content(request):

    return render(request, 'order/order.html')
def order_complete(request):
    return HttpResponse("Order Complete")
