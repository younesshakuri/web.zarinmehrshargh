from django.shortcuts import get_object_or_404, render

from inquiries.forms import capture_inquiry
from inquiries.models import Inquiry
from products.models import Category, Product


def product_list(request):
    categories = Category.objects.filter(is_active=True).prefetch_related("products")
    return render(request, "products/list.html", {"categories": categories})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    form, response = capture_inquiry(request, Inquiry.Kind.QUOTE, product)
    if response:
        return response
    related = (
        Product.objects.filter(is_active=True, category=product.category)
        .exclude(pk=product.pk)[:3]
    )
    return render(
        request,
        "products/detail.html",
        {"product": product, "form": form, "related": related, "kind": Inquiry.Kind.QUOTE},
    )
