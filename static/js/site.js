const header = document.querySelector(".site-header");
const toggle = document.querySelector(".nav-toggle");
const bar = document.querySelector(".scroll-progress");

toggle?.addEventListener("click", () => {
  const open = header.classList.toggle("is-open");
  toggle.setAttribute("aria-expanded", open ? "true" : "false");
});

document.querySelectorAll("#site-nav a").forEach((link) => {
  link.addEventListener("click", () => {
    header.classList.remove("is-open");
    toggle?.setAttribute("aria-expanded", "false");
  });
});

const paintScroll = () => {
  header?.classList.toggle("is-scrolled", window.scrollY > 8);
  const max = document.documentElement.scrollHeight - window.innerHeight;
  if (bar) bar.style.transform = `scaleX(${max > 0 ? window.scrollY / max : 0})`;
};
paintScroll();
window.addEventListener("scroll", paintScroll, { passive: true });

const canvas = document.querySelector(".dust");
const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
if (canvas && !reduce) {
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


/* ===== ZARIN HERO SLIDER ===== */

function initZarinHeroSlider() {
    const carousel = document.getElementById("heroCarousel");

    if (!carousel) return;

    const slides = Array.from(
        carousel.querySelectorAll(".hero-slide")
    );

    const dots = Array.from(
        carousel.querySelectorAll(".hero-dot")
    );

    if (slides.length <= 1) return;

    let currentIndex = 0;
    let timer = null;

    const delay = 5000;
    const reduceMotion = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    ).matches;

    function showSlide(index) {
        currentIndex = (index + slides.length) % slides.length;

        slides.forEach((slide, i) => {
            const isActive = i === currentIndex;

            slide.classList.toggle("active", isActive);
            slide.setAttribute(
                "aria-hidden",
                isActive ? "false" : "true"
            );
        });

        dots.forEach((dot, i) => {
            const isActive = i === currentIndex;

            dot.classList.toggle("active", isActive);
            dot.setAttribute(
                "aria-current",
                isActive ? "true" : "false"
            );
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

if (document.readyState === "loading") {
    document.addEventListener(
        "DOMContentLoaded",
        initZarinHeroSlider
    );
} else {
    initZarinHeroSlider();
}
