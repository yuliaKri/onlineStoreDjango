from django.contrib import admin
# Register your models here.
from .models import *

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'old_price', 'quantity', 'brand']
    search_fields = ['title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'category']

class ProductReviewAdmin(admin.ModelAdmin):
   list_display = ['product', 'review']

admin.site.register(ProductReview, ProductReviewAdmin)
