from django.contrib import admin

from products.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug", "description", "created_at"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name", "description"]
    ordering = ["id"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "slug",
        "price",
        "stock",
        "category",
        "is_active",
        "created_at",
    ]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = [
        "is_active",
        "category",
    ]
    search_fields = ["name", "description"]
    ordering = ["id"]
