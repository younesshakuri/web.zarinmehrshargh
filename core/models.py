from django.db import models

from core.i18n import Translatable


class SiteProfile(Translatable):
    """Single company record edited from the admin."""

    name_fa = models.CharField(max_length=200, verbose_name="نام شرکت فارسی")
    name_en = models.CharField(max_length=200, verbose_name="نام شرکت انگلیسی")
    slogan_fa = models.CharField(max_length=300, verbose_name="شعار فارسی")
    slogan_en = models.CharField(max_length=300, verbose_name="شعار انگلیسی")
    intro_fa = models.TextField(verbose_name="معرفی کوتاه فارسی")
    intro_en = models.TextField(verbose_name="معرفی کوتاه انگلیسی")
    about_fa = models.TextField(verbose_name="درباره شرکت فارسی")
    about_en = models.TextField(verbose_name="درباره شرکت انگلیسی")
    trade_fa = models.TextField(verbose_name="متن بازرگانی فارسی")
    trade_en = models.TextField(verbose_name="متن بازرگانی انگلیسی")
    phone = models.CharField(max_length=40, verbose_name="تلفن")
    whatsapp = models.CharField(max_length=40, blank=True, verbose_name="واتساپ")
    email = models.EmailField(verbose_name="ایمیل")
    address_fa = models.CharField(max_length=300, verbose_name="آدرس فارسی")
    address_en = models.CharField(max_length=300, verbose_name="آدرس انگلیسی")
    hours_fa = models.CharField(max_length=200, blank=True, verbose_name="ساعات کاری فارسی")
    hours_en = models.CharField(max_length=200, blank=True, verbose_name="ساعات کاری انگلیسی")
    instagram_url = models.URLField(blank=True, verbose_name="اینستاگرام")

    class Meta:
        verbose_name = "مشخصات شرکت"
        verbose_name_plural = "مشخصات شرکت"

    def __str__(self):
        return self.name_fa

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _created = cls.objects.get_or_create(
            pk=1,
            defaults={
                "name_fa": "شرکت زعفران زرین مهر شرق",
                "name_en": "Zarin Mehr Shargh Saffron Company",
                "slogan_fa": "اصالت، ریشه در طبیعت؛ کیفیت، امضای زرین ما",
                "slogan_en": "Authenticity rooted in nature; quality signed in gold.",
                "intro_fa": "",
                "intro_en": "",
                "about_fa": "",
                "about_en": "",
                "trade_fa": "",
                "trade_en": "",
                "phone": "",
                "email": "info@example.com",
                "address_fa": "",
                "address_en": "",
            },
        )
        return obj


class CompanyValue(Translatable):
    title_fa = models.CharField(max_length=150, verbose_name="عنوان فارسی")
    title_en = models.CharField(max_length=150, verbose_name="عنوان انگلیسی")
    text_fa = models.TextField(verbose_name="متن فارسی")
    text_en = models.TextField(verbose_name="متن انگلیسی")
    display_order = models.PositiveIntegerField(default=0, verbose_name="ترتیب")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        verbose_name = "ارزش شرکت"
        verbose_name_plural = "ارزش‌های شرکت"
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title_fa


class GalleryItem(Translatable):
    title_fa = models.CharField(max_length=180, verbose_name="عنوان فارسی")
    title_en = models.CharField(max_length=180, verbose_name="عنوان انگلیسی")
    caption_fa = models.CharField(max_length=300, blank=True, verbose_name="توضیح فارسی")
    caption_en = models.CharField(max_length=300, blank=True, verbose_name="توضیح انگلیسی")
    image = models.ImageField(
        upload_to="gallery/",
        blank=True,
        verbose_name="تصویر",
    )
    display_order = models.PositiveIntegerField(default=0, verbose_name="ترتیب")
    is_active = models.BooleanField(default=True, verbose_name="نمایش در سایت")

    class Meta:
        verbose_name = "تصویر گالری"
        verbose_name_plural = "گالری"
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title_fa
