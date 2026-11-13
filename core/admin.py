from django.contrib import admin

from core.models import CompanyValue, GalleryItem, SiteProfile


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteProfile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    fieldsets = (
        ("هویت", {"fields": ("name_fa", "name_en", "slogan_fa", "slogan_en")}),
        ("متن‌ها", {"fields": ("intro_fa", "intro_en", "about_fa", "about_en", "trade_fa", "trade_en")}),
        ("تماس", {"fields": ("phone", "whatsapp", "email", "address_fa", "address_en", "hours_fa", "hours_en", "instagram_url")}),
    )


@admin.register(CompanyValue)
class CompanyValueAdmin(admin.ModelAdmin):
    list_display = ("title_fa", "display_order", "is_active")
    list_editable = ("display_order", "is_active")
    search_fields = ("title_fa", "title_en")


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ("title_fa", "display_order", "is_active")
    list_editable = ("display_order", "is_active")
    search_fields = ("title_fa", "title_en")
