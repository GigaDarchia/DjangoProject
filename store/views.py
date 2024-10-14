from django.http import JsonResponse
from django.shortcuts import render
from .models import Product, Category
from django.db.models import Max, Min, Avg, Sum

def store(request):
    return render(request, 'store/store.html')

def category(request):
    category_list = Category.objects.filter(parent=None)
    return render(request, 'store/category.html', {"categories": category_list})

def products(request, category_id):

    category = Category.objects.get(id=category_id)
    subcategories = category.get_subcategories()
    categories = [category]+subcategories

    products = Product.objects.filter(category__in=categories).prefetch_related('category')

    statistics = products.aggregate(
        max_price=Max('price'),
        min_price=Min('price'),
        avg_price=Avg('price'),
        total_cost = Sum('price')*Sum('quantity')
    )

    return render(request, 'store/products.html', context={"products": products,
                                                           "statistics": statistics,
                                                           "category": category})

def product(request, product_id):
    return render(request, "store/product.html", context={"product": Product.objects.get(id=product_id)})

def categories_json(request):
    category_list = []

    for category in Category.objects.all():
        category_list.append({
            'id': category.id,
            "name": category.name,
            "img": category.img.name if category.img else None,
            "parent": {
                "id": category.parent.id,
                "name": category.parent.name
              } if category.parent else None
        })

    return JsonResponse(category_list, safe=False)

def products_json(request):
    product_list = []

    for product in Product.objects.all():
        category_list = []
        for category in product.category.all():
            category_list.append({
                'id': category.id,
                'name': category.name
            })

        product_list.append({
            'id': product.id,
            'name': product.title,
            'price': product.price,
            'quantity': product.quantity,
            'image': product.img.name if product.img else None,
            "description": product.desc if product.desc else None,
            'categories': category_list if product.category.count() > 0 else None
        })

    return JsonResponse(product_list, safe=False)

