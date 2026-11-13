from django.db import models


class Inquiry(models.Model):
    class Kind(models.TextChoices):
        QUOTE = "quote", "استعلام قیمت"
        PARTNERSHIP = "partnership", "درخواست همکاری"
        CONTACT = "contact", "پیام تماس"

    class Status(models.TextChoices):
        NEW = "new", "جدید"
        REVIEWING = "reviewing", "در حال بررسی"
        ANSWERED = "answered", "پاسخ‌داده‌شده"
        CLOSED = "closed", "بسته‌شده"

    kind = models.CharField(
        max_length=20,
        choices=Kind.choices,
        default=Kind.CONTACT,
        verbose_name="نوع درخواست",
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
        verbose_name="وضعیت",
    )
    full_name = models.CharField(max_length=150, verbose_name="نام و نام خانوادگی")
    company_name = models.CharField(max_length=180, blank=True, verbose_name="نام شرکت")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=40, blank=True, verbose_name="تلفن")
    country = models.CharField(max_length=80, blank=True, verbose_name="کشور")
    subject = models.CharField(max_length=200, blank=True, verbose_name="موضوع")
    message = models.TextField(verbose_name="پیام")
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="inquiries",
        verbose_name="محصول مرتبط",
    )
    internal_note = models.TextField(blank=True, verbose_name="یادداشت داخلی")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    class Meta:
        verbose_name = "درخواست"
        verbose_name_plural = "درخواست‌ها"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.get_kind_display()} — {self.full_name}"
