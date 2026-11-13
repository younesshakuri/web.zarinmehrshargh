from django import forms

from core.ui import UI
from inquiries.models import Inquiry


class InquiryForm(forms.ModelForm):
    company_site = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"tabindex": "-1", "autocomplete": "off", "aria-hidden": "true"}
        ),
    )

    class Meta:
        model = Inquiry
        fields = [
            "full_name",
            "company_name",
            "email",
            "phone",
            "country",
            "subject",
            "message",
        ]
        widgets = {"message": forms.Textarea(attrs={"rows": 5})}

    def __init__(self, *args, language="fa", **kwargs):
        super().__init__(*args, **kwargs)
        copy = UI[language]
        for name, field in self.fields.items():
            if name == "company_site":
                continue
            field.label = copy["fields"][name]["label"]
            field.widget.attrs["placeholder"] = copy["fields"][name]["placeholder"]
            field.widget.attrs["class"] = "control"
            field.error_messages["required"] = copy["required"]
        self.fields["email"].error_messages["invalid"] = copy["invalid_email"]


def capture_inquiry(request, kind, product=None):
    from django.contrib import messages
    from django.shortcuts import redirect

    language = "en" if str(request.LANGUAGE_CODE).lower().startswith("en") else "fa"
    if request.method == "POST":
        form = InquiryForm(request.POST, language=language)
        if form.is_valid():
            if not form.cleaned_data.get("company_site"):
                inquiry = form.save(commit=False)
                inquiry.kind = kind
                inquiry.product = product
                inquiry.save()
            messages.success(request, UI[language]["sent"])
            return form, redirect(request.get_full_path())
        return form, None
    return InquiryForm(language=language), None
