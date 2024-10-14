from django.db import models
from django.db.models import Model

class Product(Model):
    title = models.CharField(max_length=255)
    category = models.ManyToManyField('Category', related_name='products', blank=True)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    img = models.ImageField(upload_to='products', null=True, blank=True)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Category(Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    img = models.ImageField(upload_to='categories', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_subcategories(self):
        subcategories = []
        children = Category.objects.filter(parent=self)
        for child in children:
            subcategories.append(child)
            subcategories.extend(child.get_subcategories())
        return subcategories

