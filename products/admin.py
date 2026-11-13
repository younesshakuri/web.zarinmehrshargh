from django.contrib import admin

from products.models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name_fa", "name_en", "display_order", "is_active")
    list_editable = ("display_order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name_fa", "name_en")
    prepopulated_fields = {"slug": ("name_en",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name_fa", "category", "is_featured", "is_active", "display_order")
    list_editable = ("is_featured", "is_active", "display_order")
    list_filter = ("category", "is_featured", "is_active")
    search_fields = ("name_fa", "name_en")
    prepopulated_fields = {"slug": ("name_en",)}
    inlines = [ProductImageInline]
    fieldsets = (
        ("نام", {"fields": ("category", "name_fa", "name_en", "slug")}),
        ("توضیح", {"fields": ("short_description_fa", "short_description_en", "description_fa", "description_en")}),
        ("نمایش", {"fields": ("main_image", "is_featured", "is_active", "display_order")}),
    )
