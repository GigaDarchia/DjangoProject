from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('name', 'parent')
    list_editable = ('parent',)
    autocomplete_fields = ('parent',)
    search_fields = ('name',)
    empty_value_display = '-None-'

    fieldsets = [
        (
            None,
            {
                'fields': ['name', 'parent']
            },
        ),
        (
            'Advanced options',
            {
                'classes': ('collapse',),
                'fields': ['img']
            }
        )]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity', 'get_categories')
    list_filter = ('price', 'title')
    search_fields = ('title', 'category__name')
    list_editable = ('price', 'quantity')
    autocomplete_fields = ('category',)
    filter_horizontal = ('category',)
    empty_value_display = '-None-'
    fieldsets = [
        (
            None,
            {
                'fields': ['title', 'price', 'quantity', 'category']
            },
        ),
        (
            'Advanced options',
            {
                'classes': ('collapse',),
                'fields': ['img', 'desc']
            }
        )
    ]

    @admin.display(description='Categories')
    def get_categories(self, obj):
        return list(obj.category.all())

    # @admin.action()  Add actions (like in WordPress)


