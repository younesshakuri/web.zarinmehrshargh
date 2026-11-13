from core.models import SiteProfile
from core.ui import UI


def company(request):
    code = getattr(request, "LANGUAGE_CODE", "fa") or "fa"
    lang = "en" if str(code).lower().startswith("en") else "fa"
    return {
        "profile": SiteProfile.load(),
        "lang": lang,
        "ui": UI[lang],
        "page_dir": "ltr" if lang == "en" else "rtl",
    }
