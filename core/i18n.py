from django.db import models


class Translatable(models.Model):
    """Pick ``field_fa`` or ``field_en`` from the active language."""

    class Meta:
        abstract = True

    def translated(self, field, language_code):
        code = "en" if str(language_code or "").lower().startswith("en") else "fa"
        value = getattr(self, f"{field}_{code}", "") or ""
        if value:
            return value
        fallback = "fa" if code == "en" else "en"
        return getattr(self, f"{field}_{fallback}", "") or ""
