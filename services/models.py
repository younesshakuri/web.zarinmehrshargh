from django.db import models

from core.i18n import Translatable


class Service(Translatable):
    name_fa = models.CharField(max_length=200, verbose_name="نام خدمت فارسی")
    name_en = models.CharField(max_length=200, verbose_name="نام خدمت انگلیسی")
    slug = models.SlugField(max_length=220, unique=True, verbose_name="شناسه URL")
    summary_fa = models.CharField(max_length=300, verbose_name="خلاصه فارسی")
    summary_en = models.CharField(max_length=300, verbose_name="خلاصه انگلیسی")
    description_fa = models.TextField(verbose_name="توضیحات فارسی")
    description_en = models.TextField(verbose_name="توضیحات انگلیسی")
    image = models.ImageField(upload_to="services/", blank=True, verbose_name="تصویر")
    display_order = models.PositiveIntegerField(default=0, verbose_name="ترتیب")
    is_active = models.BooleanField(default=True, verbose_name="نمایش در سایت")

    class Meta:
        verbose_name = "خدمت"
        verbose_name_plural = "خدمات"
        ordering = ["display_order", "name_fa"]

    def __str__(self):
        return self.name_fa
