document.addEventListener("DOMContentLoaded", () => {
    const header = document.querySelector(".site-header");
    const toggle = document.querySelector(".nav-toggle");
    const bar = document.querySelector(".scroll-progress");

    function closeMobileMenu() {
        header?.classList.remove("is-open");
        toggle?.setAttribute("aria-expanded", "false");
    }

    toggle?.addEventListener("click", () => {
        const isOpen = header.classList.toggle("is-open");
        toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });

    // Close after clicking a navigation link (fixed selector to match class .site-nav)
    document.querySelectorAll(".site-nav a").forEach((link) => {
        link.addEventListener("click", closeMobileMenu);
    });

    // Close when clicking outside the header
    document.addEventListener("click", (event) => {
        if (
            header &&
            !header.contains(event.target) &&
            header.classList.contains("is-open")
        ) {
            closeMobileMenu();
        }
    });

    // Close with Escape key
    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            closeMobileMenu();
            toggle?.focus();
        }
    });

    // Close when returning to desktop layout
    window.addEventListener("resize", () => {
        if (window.innerWidth > 900) {
            closeMobileMenu();
        }
    });

    // Scroll progress & header shadow
    const paintScroll = () => {
        header?.classList.toggle("is-scrolled", window.scrollY > 8);
        const max = document.documentElement.scrollHeight - window.innerHeight;
        if (bar) bar.style.transform = `scaleX(${max > 0 ? window.scrollY / max : 0})`;
    };
    paintScroll();
    window.addEventListener("scroll", paintScroll, { passive: true });

    // Dust Canvas Animation
    const canvas = document.querySelector(".dust");
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (canvas && !reduceMotion) {
        const context = canvas.getContext("2d");
        const dots = Array.from({ length: 42 }, () => ({
            x: Math.random(),
            y: Math.random(),
            r: Math.random() * 1.4 + 0.3,
            s: Math.random() * 0.25 + 0.05,
        }));
        
        const resize = () => {
            const rect = canvas.getBoundingClientRect();
            canvas.width = rect.width;
            canvas.height = rect.height;
        };
        resize();
        window.addEventListener("resize", resize);

        const draw = () => {
            context.clearRect(0, 0, canvas.width, canvas.height);
            dots.forEach((dot) => {
                dot.y -= dot.s / 400;
                if (dot.y < 0) dot.y = 1;
                context.beginPath();
                context.fillStyle = "rgba(243, 221, 176, .55)";
                context.arc(dot.x * canvas.width, dot.y * canvas.height, dot.r, 0, Math.PI * 2);
                context.fill();
            });
            requestAnimationFrame(draw);
        };
        draw();
    }

    // ===== ZARIN HERO SLIDER ===== *
    function initZarinHeroSlider() {
        const carousel = document.getElementById("heroCarousel");
        if (!carousel) return;

        const slides = Array.from(carousel.querySelectorAll(".hero-slide"));
        const dots = Array.from(carousel.querySelectorAll(".hero-dot"));

        if (slides.length <= 1) return;

        let currentIndex = 0;
        let timer = null;
        const delay = 5000;

        function showSlide(index) {
            currentIndex = (index + slides.length) % slides.length;

            slides.forEach((slide, i) => {
                const isActive = i === currentIndex;
                slide.classList.toggle("active", isActive);
                slide.setAttribute("aria-hidden", isActive ? "false" : "true");
            });

            dots.forEach((dot, i) => {
                const isActive = i === currentIndex;
                dot.classList.toggle("active", isActive);
                dot.setAttribute("aria-current", isActive ? "true" : "false");
            });
        }

        function stopSlider() {
            if (timer !== null) {
                clearInterval(timer);
                timer = null;
            }
        }

        function startSlider() {
            stopSlider();
            if (reduceMotion) return;

            timer = setInterval(() => {
                showSlide(currentIndex + 1);
            }, delay);
        }

        dots.forEach((dot, index) => {
            dot.addEventListener("click", () => {
                showSlide(index);
                startSlider();
            });
        });

        carousel.addEventListener("mouseenter", stopSlider);
        carousel.addEventListener("mouseleave", startSlider);

        document.addEventListener("visibilitychange", () => {
            if (document.hidden) {
                stopSlider();
            } else {
                startSlider();
            }
        });

        showSlide(0);
        startSlider();
    }

    initZarinHeroSlider();
});