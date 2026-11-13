from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
    verbose_name = "محتوای اصلی"

    def ready(self):
        from django.contrib import admin

        admin.site.site_header = "زرین مهر شرق"
        admin.site.site_title = "پنل زرین مهر شرق"
        admin.site.index_title = "مدیریت محتوای سایت"
