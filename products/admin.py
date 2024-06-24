from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stars')
    search_fields = ('name', 'category')
    list_filter = ('category', 'stars')

admin.site.register(Product, ProductAdmin)

