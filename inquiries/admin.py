from django.contrib import admin

from inquiries.models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("full_name", "kind", "status", "product", "created_at")
    list_filter = ("kind", "status", "created_at")
    search_fields = ("full_name", "company_name", "email", "phone", "subject")
    readonly_fields = ("created_at",)
    autocomplete_fields = ("product",)
    fieldsets = (
        ("درخواست", {"fields": ("kind", "status", "product", "subject", "message", "created_at")}),
        ("فرستنده", {"fields": ("full_name", "company_name", "email", "phone", "country")}),
        ("داخلی", {"fields": ("internal_note",)}),
    )
