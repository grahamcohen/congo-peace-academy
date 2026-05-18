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
      document.body.style.overflow = !isOpen ? 'hidden' : '';
    });

    // close on escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && navList.getAttribute('data-open') === 'true') {
        navList.setAttribute('data-open', 'false');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
        toggle.focus();
      }
    });

    // close when clicking a link (mobile)
    navList.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        if (window.innerWidth < 1024) {
          navList.setAttribute('data-open', 'false');
          toggle.setAttribute('aria-expanded', 'false');
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
  // Header shadow on scroll
  // ---------------------------------------------------------------------
  const header = document.querySelector('.site-header');
  if (header) {
    let lastY = 0;
    const onScroll = function () {
      const y = window.scrollY;
      if (y > 8 && lastY <= 8) {
        header.style.boxShadow = '0 2px 12px rgba(15, 22, 20, 0.05)';
      } else if (y <= 8 && lastY > 8) {
        header.style.boxShadow = '';
      }
      lastY = y;
    };
    window.addEventListener('scroll', onScroll, { passive: true });
  }
})();
