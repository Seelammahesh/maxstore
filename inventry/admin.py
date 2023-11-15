from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','color']
    search_fields=['name','color','brand_name']
    list_filter=['brand_name','price']


admin.site.register(Product,ProductAdmin)
