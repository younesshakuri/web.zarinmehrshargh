from django.core.management.base import BaseCommand

from core.models import CompanyValue, GalleryItem, SiteProfile
from products.models import Category, Product
from services.models import Service


class Command(BaseCommand):
    help = "Fill the site with sample company content. Safe to run again."

    def handle(self, *args, **options):
        profile, _created = SiteProfile.objects.update_or_create(
            pk=1,
            defaults={
                "name_fa": "شرکت زعفران زرین مهر شرق",
                "name_en": "Zarin Mehr Shargh Saffron Company",
                "slogan_fa": "اصالت، ریشه در طبیعت؛ کیفیت، امضای زرین ما",
                "slogan_en": "Authenticity rooted in nature; quality signed in gold.",
                "intro_fa": (
                    "زرین مهر شرق در بسته‌بندی سرگل و گل زعفران، تولید فرآورده‌های زعفرانی، "
                    "سورتینگ محصولات کشاورزی و بازرگانی مواد غذایی فعالیت می‌کند. "
                    "این سایت برای معرفی شرکت و دریافت استعلام خریداران عمده است."
                ),
                "intro_en": (
                    "Zarin Mehr Shargh packs sargol and saffron flowers, produces saffron goods, "
                    "sorts agricultural crops, and trades food products. "
                    "This site introduces the company and receives wholesale inquiries."
                ),
                "about_fa": (
                    "فعالیت شرکت بر کیفیت دسته‌بندی، بسته‌بندی دقیق و عرضهٔ عمده بنا شده است. "
                    "از مزرعه تا بستهٔ نهایی، جداسازی و کنترل چشمی بخشی از کار روزمرهٔ ماست. "
                    "متن و اطلاعات تماس فعلی نمونه‌اند و از پنل مدیریت جایگزین می‌شوند."
                ),
                "about_en": (
                    "The company is built around careful grading, precise packing, and wholesale supply. "
                    "From the field to the finished pack, sorting and visual control are part of the daily work. "
                    "The current text and contact details are samples and can be replaced from the admin."
                ),
                "trade_fa": (
                    "بخش بازرگانی زرین مهر شرق برای خریداران عمده، واردکنندگان و همکاران تجاری است. "
                    "عمده‌فروشی مواد غذایی و آشامیدنی در کنار زعفران انجام می‌شود و قیمت، "
                    "پس از بررسی مقدار و مشخصات سفارش اعلام می‌گردد."
                ),
                "trade_en": (
                    "The trading desk serves wholesalers, importers, and commercial partners. "
                    "Food and beverage wholesale sits alongside saffron, and prices are quoted "
                    "after the quantity and specification of each order are reviewed."
                ),
                "phone": "051-38000000",
                "whatsapp": "989150000000",
                "email": "info@zarinmehrshargh.ir",
                "address_fa": "مشهد، خراسان رضوی — آدرس نمونه",
                "address_en": "Mashhad, Razavi Khorasan — sample address",
                "hours_fa": "شنبه تا چهارشنبه، ۸ تا ۱۶",
                "hours_en": "Saturday to Wednesday, 8:00 to 16:00",
                "instagram_url": "https://instagram.com/",
            },
        )

        values = [
            ("اصالت", "Origin", "زعفران را با نام مبدأ و درجهٔ واقعی عرضه می‌کنیم.", "Saffron is offered with its real origin and grade.", 1),
            ("دقت در بسته‌بندی", "Precise packing", "وزن، جنس بسته و ظاهر نهایی پیش از خروج کنترل می‌شود.", "Weight, pack material, and finish are checked before dispatch.", 2),
            ("همکاری عمده", "Wholesale partnership", "پاسخ استعلام بر اساس حجم، مقصد و نوع بسته‌بندی تنظیم می‌شود.", "Quotes follow volume, destination, and the required pack.", 3),
        ]
        for title_fa, title_en, text_fa, text_en, order in values:
            CompanyValue.objects.update_or_create(
                title_en=title_en,
                defaults={
                    "title_fa": title_fa,
                    "text_fa": text_fa,
                    "text_en": text_en,
                    "display_order": order,
                    "is_active": True,
                },
            )

        gallery = [
            ("بسته‌بندی سرگل", "Sargol packing", "خط بسته‌بندی سرگل", "Sargol packing line", 1),
            ("سورتینگ محصول", "Crop sorting", "جداسازی و یکدست‌سازی", "Grading and sorting", 2),
            ("بستهٔ صادراتی", "Export pack", "آماده‌سازی سفارش عمده", "Wholesale order preparation", 3),
        ]
        for title_fa, title_en, caption_fa, caption_en, order in gallery:
            GalleryItem.objects.update_or_create(
                title_en=title_en,
                defaults={
                    "title_fa": title_fa,
                    "caption_fa": caption_fa,
                    "caption_en": caption_en,
                    "display_order": order,
                    "is_active": True,
                },
            )

        saffron, _ = Category.objects.update_or_create(
            slug="packaged-saffron",
            defaults={
                "name_fa": "زعفران بسته‌بندی‌شده",
                "name_en": "Packaged saffron",
                "description_fa": "سرگل، نگین، پوشال و گل زعفران در بسته‌های عمده.",
                "description_en": "Sargol, negin, pushal, and saffron flower in wholesale packs.",
                "display_order": 1,
                "is_active": True,
            },
        )
        derivatives, _ = Category.objects.update_or_create(
            slug="saffron-derivatives",
            defaults={
                "name_fa": "فرآورده‌های زعفران",
                "name_en": "Saffron derivatives",
                "description_fa": "فرآورده‌هایی که از زعفران درجه‌بندی‌شده تولید و بسته‌بندی می‌شوند.",
                "description_en": "Goods produced and packed from graded saffron.",
                "display_order": 2,
                "is_active": True,
            },
        )

        products = [
            (saffron, "premium-sargol", "سرگل ممتاز", "Premium sargol", "رشته‌های سرگل، یکدست و مناسب بستهٔ عمده.", "Even sargol threads for wholesale packs.", "سرگل از بخش بالایی کلاله جدا می‌شود و برای خریدارانی مناسب است که ظاهر یکدست و رنگ پایدار می‌خواهند. حداقل سفارش و نوع بسته پس از استعلام اعلام می‌شود.", "Sargol is taken from the upper stigma. It suits buyers who want an even appearance and a stable color. Minimum order and pack type are confirmed with the quote.", True, 1),
            (saffron, "saffron-flower", "گل زعفران", "Saffron flower", "گل کامل برای خشک‌کردن، جداسازی یا بسته‌بندی.", "Whole flowers for drying, separating, or packing.", "گل زعفران برای مجموعه‌هایی عرضه می‌شود که جداسازی یا بسته‌بندی را در مقصد خود ادامه می‌دهند. رطوبت و نحوهٔ ارسال در استعلام مشخص می‌شود.", "Whole flowers are supplied to partners who continue separation or packing at their own site. Moisture and shipping method are set in the quote.", True, 2),
            (saffron, "negin-saffron", "نگین زعفران", "Negin saffron", "رشته‌های ضخیم و درشت با دسته‌بندی دقیق.", "Thick threads, carefully graded.", "نگین از درشت‌ترین رشته‌ها انتخاب می‌شود و بسته‌بندی آن برای نمایش کیفیت در بازار عمده طراحی می‌گردد.", "Negin is selected from the thickest threads and packed to present that quality in the wholesale market.", False, 3),
            (derivatives, "saffron-powder", "پودر زعفران", "Saffron powder", "پودر یکنواخت برای تولید و بسته‌بندی مجدد.", "An even powder for production and repacking.", "پودر از زعفران درجه‌بندی‌شده آسیاب می‌شود و برای کارگاه‌های تولید مواد غذایی و بسته‌بندی مجدد مناسب است.", "The powder is milled from graded saffron and suits food workshops and repacking lines.", False, 4),
        ]
        for category, slug, name_fa, name_en, short_fa, short_en, desc_fa, desc_en, featured, order in products:
            Product.objects.update_or_create(
                slug=slug,
                defaults={
                    "category": category,
                    "name_fa": name_fa,
                    "name_en": name_en,
                    "short_description_fa": short_fa,
                    "short_description_en": short_en,
                    "description_fa": desc_fa,
                    "description_en": desc_en,
                    "is_featured": featured,
                    "is_active": True,
                    "display_order": order,
                },
            )

        services = [
            ("sargol-packing", "بسته‌بندی سرگل و گل زعفران", "Sargol and flower packing", "بسته‌بندی رشته و گل با وزن و ظاهر یکسان.", "Packing threads and flowers to a consistent weight and finish.", "جداسازی، توزین و چیدن در قوطی یا بستهٔ مورد توافق خریدار. جنس بسته و برچسب در سفارش مشخص می‌شود.", "Separation, weighing, and placing into the tin or pack agreed with the buyer. Material and label are set per order."),
            ("saffron-goods", "تولید و بسته‌بندی فرآورده زعفران", "Saffron goods production", "تبدیل زعفران درجه‌بندی‌شده به فرآورده و بستهٔ نهایی.", "Turning graded saffron into a finished good and pack.", "آسیاب، ترکیب و بسته‌بندی فرآورده زیر نظر همان استانداردی که برای محصول خام رعایت می‌شود.", "Milling, blending, and packing under the same care used for the raw crop."),
            ("crop-sorting", "سورتینگ محصولات کشاورزی", "Agricultural sorting", "دسته‌بندی و یکدست‌سازی فرآورده‌های زراعی.", "Grading agricultural crops into even lots.", "جداسازی بر اساس اندازه، سلامت و ظاهر، سپس بسته‌بندی برای انبار یا ارسال عمده.", "Sorting by size, soundness, and appearance, then packing for storage or wholesale dispatch."),
            ("farm-contracting", "پیمانکاری امور زراعی", "Farm contracting", "انجام کارهای زراعی به‌صورت پیمانکاری.", "Agricultural work carried out under contract.", "آماده‌سازی، داشت و برداشت طبق توافق مزرعه. محدودهٔ کار و زمان‌بندی در قرارداد می‌آید.", "Preparation, crop care, and harvest as agreed with the farm. Scope and timing sit in the contract."),
            ("food-wholesale", "عمده‌فروشی مواد غذایی و آشامیدنی", "Food and beverage wholesale", "تأمین عمده برای فروشگاه، کارگاه و بازرگان.", "Wholesale supply for shops, workshops, and traders.", "زعفران در کنار سایر اقلام غذایی و آشامیدنی، با اعلام موجودی و قیمت پس از استعلام.", "Saffron alongside other food and drink items, with availability and price after inquiry."),
            ("trading-desk", "بازرگانی", "Trading", "هماهنگی خرید، فروش و ارسال سفارش‌های تجاری.", "Coordinating purchase, sale, and dispatch of commercial orders.", "پیگیری سفارش از اعلام مشخصات تا آماده‌سازی مدارک و ارسال. این بخش ویترین قیمت آنلاین نیست.", "Following an order from specification to documents and dispatch. This desk is not an online price list."),
        ]
        for order, item in enumerate(services, start=1):
            slug, name_fa, name_en, summary_fa, summary_en, description_fa, description_en = item
            Service.objects.update_or_create(
                slug=slug,
                defaults={
                    "name_fa": name_fa,
                    "name_en": name_en,
                    "summary_fa": summary_fa,
                    "summary_en": summary_en,
                    "description_fa": description_fa,
                    "description_en": description_en,
                    "display_order": order,
                    "is_active": True,
                },
            )

        self.stdout.write(self.style.SUCCESS(f"Sample content is ready for {profile.name_fa}."))
