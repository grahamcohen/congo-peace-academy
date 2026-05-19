/* =====================================================================
   Congo Peace Academy — main.js
   Mobile nav, scroll reveal, smooth interactions
   ===================================================================== */

(function () {
  'use strict';

  // ---------------------------------------------------------------------
  // Mobile nav toggle
  // ---------------------------------------------------------------------
  const toggle = document.querySelector('.nav-toggle');
  const navList = document.querySelector('.nav-list');

  if (toggle && navList) {
    toggle.addEventListener('click', function () {
      const isOpen = navList.getAttribute('data-open') === 'true';
      navList.setAttribute('data-open', String(!isOpen));
      toggle.setAttribute('aria-expanded', String(!isOpen));
      document.body.setAttribute('data-nav-open', String(!isOpen));
      document.body.style.overflow = !isOpen ? 'hidden' : '';
    });

    // close on escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && navList.getAttribute('data-open') === 'true') {
        navList.setAttribute('data-open', 'false');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.setAttribute('data-nav-open', 'false');
        document.body.style.overflow = '';
        toggle.focus();
      }
    });

    // tap outside to close (mobile)
    document.addEventListener('click', function (e) {
      if (navList.getAttribute('data-open') !== 'true') return;
      if (navList.contains(e.target) || toggle.contains(e.target)) return;
      navList.setAttribute('data-open', 'false');
      toggle.setAttribute('aria-expanded', 'false');
      document.body.setAttribute('data-nav-open', 'false');
      document.body.style.overflow = '';
    });

    // close when clicking a link (mobile)
    navList.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        if (window.innerWidth < 1024) {
          navList.setAttribute('data-open', 'false');
          toggle.setAttribute('aria-expanded', 'false');
          document.body.setAttribute('data-nav-open', 'false');
          document.body.style.overflow = '';
        }
      });
    });
  }

  // ---------------------------------------------------------------------
  // Scroll reveal — adds .is-visible to .reveal elements as they enter viewport
  // ---------------------------------------------------------------------
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if ('IntersectionObserver' in window && !reduced) {
    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );
    document.querySelectorAll('.reveal').forEach(function (el) {
      observer.observe(el);
    });
  } else {
    // reduced motion or no IntersectionObserver — show everything immediately
    document.querySelectorAll('.reveal').forEach(function (el) {
      el.classList.add('is-visible');
    });
  }

  // ---------------------------------------------------------------------
  // Header: shadow + is-scrolled class as you scroll past the hero
  // ---------------------------------------------------------------------
  const header = document.querySelector('.site-header');
  if (header) {
    const onScroll = function () {
      const y = window.scrollY;
      header.classList.toggle('is-scrolled', y > 80);
      header.style.boxShadow = y > 8 ? '0 2px 12px rgba(15, 22, 20, 0.05)' : '';
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // ---------------------------------------------------------------------
  // Hero background video: fade in once it has started playing
  // ---------------------------------------------------------------------
  const heroVideo = document.querySelector('.hero-bg-video');
  if (heroVideo) {
    // YouTube iframe takes a beat to load — fade in after a delay
    setTimeout(function () { heroVideo.classList.add('loaded'); }, 1500);
  }

  // ---------------------------------------------------------------------
  // Image fallback — if any <img> 404s, swap to a known-good image so the
  // page never shows broken icons. Cycles through a small pool of fallbacks.
  // ---------------------------------------------------------------------
  const fallbackPool = [
    'assets/images/header_background_image.jpg',
    'assets/images/education_image.jpg',
    'assets/images/peacebuilding_image.jpg',
    'assets/images/foundation-for-farming_image.jpg',
    'assets/images/relief-and-assistance_image.jpg',
    'assets/images/most-recent-events_image.jpg',
  ];
  let fbIdx = 0;
  // Compute prefix to /assets based on current page depth
  const depth = (location.pathname.replace(/\/$/, '').split('/').length - 2);
  const prefix = depth > 0 ? '../'.repeat(depth - 1) : '';
  document.querySelectorAll('img').forEach(function (img) {
    img.addEventListener('error', function handleErr() {
      img.removeEventListener('error', handleErr);
      const next = fallbackPool[fbIdx++ % fallbackPool.length];
      img.src = prefix + next;
    });
  });
})();
