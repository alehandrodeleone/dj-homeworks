from django.contrib import admin
from .models import Product,StockProduct,Stock
@admin.register(Product)
class adminproduct(admin.ModelAdmin):
    list_display=['title','description']

