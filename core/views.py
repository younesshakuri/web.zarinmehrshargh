from django.shortcuts import render

from core.models import CompanyValue, GalleryItem
from inquiries.forms import capture_inquiry
from inquiries.models import Inquiry
from products.models import Product
from services.models import Service


def home(request):
    products = list(
        Product.objects.filter(is_active=True).select_related("category")
    )
    featured = [item for item in products if item.is_featured] or products[:2]
    return render(
        request,
        "core/home.html",
        {
            "featured": featured,
            "services": Service.objects.filter(is_active=True),
            "gallery": GalleryItem.objects.filter(is_active=True),
            "values": CompanyValue.objects.filter(is_active=True),
        },
    )


def about(request):
    return render(
        request,
        "core/about.html",
        {
            "values": CompanyValue.objects.filter(is_active=True),
            "gallery": GalleryItem.objects.filter(is_active=True),
        },
    )


def trading(request):
    form, response = capture_inquiry(request, Inquiry.Kind.PARTNERSHIP)
    if response:
        return response
    return render(
        request,
        "core/trading.html",
        {
            "form": form,
            "kind": Inquiry.Kind.PARTNERSHIP,
            "services": Service.objects.filter(is_active=True),
        },
    )


def contact(request):
    kind = request.POST.get("kind") if request.method == "POST" else request.GET.get("kind")
    if kind not in Inquiry.Kind.values:
        kind = Inquiry.Kind.CONTACT
    form, response = capture_inquiry(request, kind)
    if response:
        return response
    return render(request, "core/contact.html", {"form": form, "kind": kind})
