from django.db import models

from core.i18n import Translatable


class Category(Translatable):
    name_fa = models.CharField(max_length=150, verbose_name="نام دسته‌بندی فارسی")
    name_en = models.CharField(max_length=150, verbose_name="نام دسته‌بندی انگلیسی")
    slug = models.SlugField(max_length=180, unique=True, verbose_name="شناسه URL")
    description_fa = models.TextField(blank=True, verbose_name="توضیحات فارسی")
    description_en = models.TextField(blank=True, verbose_name="توضیحات انگلیسی")
    image = models.ImageField(
        upload_to="categories/",
        blank=True,
        verbose_name="تصویر دسته‌بندی",
    )
    display_order = models.PositiveIntegerField(default=0, verbose_name="ترتیب")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "دسته‌بندی محصول"
        verbose_name_plural = "دسته‌بندی محصولات"
        ordering = ["display_order", "name_fa"]

    def __str__(self):
        return self.name_fa


class Product(Translatable):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
        verbose_name="دسته‌بندی",
    )
    name_fa = models.CharField(max_length=200, verbose_name="نام محصول فارسی")
    name_en = models.CharField(max_length=200, verbose_name="نام محصول انگلیسی")
    slug = models.SlugField(max_length=220, unique=True, verbose_name="شناسه URL")
    short_description_fa = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="توضیح کوتاه فارسی",
    )
    short_description_en = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="توضیح کوتاه انگلیسی",
    )
    description_fa = models.TextField(blank=True, verbose_name="توضیحات کامل فارسی")
    description_en = models.TextField(blank=True, verbose_name="توضیحات کامل انگلیسی")
    main_image = models.ImageField(
        upload_to="products/",
        blank=True,
        verbose_name="تصویر اصلی محصول",
    )
    is_active = models.BooleanField(default=True, verbose_name="نمایش در سایت")
    is_featured = models.BooleanField(default=False, verbose_name="محصول ویژه")
    display_order = models.PositiveIntegerField(default=0, verbose_name="ترتیب")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین ویرایش")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return self.name_fa


class ProductImage(Translatable):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="محصول",
    )
    image = models.ImageField(upload_to="products/gallery/", verbose_name="تصویر")
    alt_fa = models.CharField(max_length=200, blank=True, verbose_name="متن جایگزین فارسی")
    alt_en = models.CharField(max_length=200, blank=True, verbose_name="متن جایگزین انگلیسی")
    display_order = models.PositiveIntegerField(default=0, verbose_name="ترتیب")

    class Meta:
        verbose_name = "تصویر محصول"
        verbose_name_plural = "تصاویر محصول"
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.alt_fa or self.product.name_fa
