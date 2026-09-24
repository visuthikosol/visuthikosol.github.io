// Mobile nav toggle
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => links.classList.remove('open'));
    });
  }

  // Scroll-triggered fade-up reveal, one-time per element.
  if ('IntersectionObserver' in window) {
    const revealItems = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealItems.forEach(item => observer.observe(item));
  } else {
    document.querySelectorAll('.reveal').forEach(item => item.classList.add('is-visible'));
  }

  // Graceful fallback: if a project photo hasn't been added yet,
  // swap the <img> for a labeled placeholder instead of a broken icon.
  document.querySelectorAll('img[data-fallback-label]').forEach(img => {
    img.addEventListener('error', () => {
      const wrap = img.closest('.card-media');
      if (!wrap) return;
      wrap.classList.add('is-empty');
      wrap.innerHTML = `<span class="mono-label">${img.dataset.fallbackLabel}<br>ADD PHOTO</span>`;
    }, { once: true });
  });
});

// Lightbox for project page images
document.addEventListener('DOMContentLoaded', () => {
  const lb = document.querySelector('.lightbox');
  if (!lb) return;
  const big = lb.querySelector('img');
  const close = () => { lb.hidden = true; big.src = ''; document.body.style.overflow = ''; };
  document.querySelectorAll('.pgrid img, .dev-media img, .final img, .split-media img, .logo-ring img, .bento img').forEach(img => {
    img.addEventListener('click', () => {
      big.src = img.currentSrc.replace(/w_\d+,h_\d+/, 'w_2000,h_2000');
      big.alt = img.alt; lb.hidden = false; document.body.style.overflow = 'hidden';
    });
  });
  lb.addEventListener('click', close);
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && !lb.hidden) close(); });
});

// Stacked sections (home products, project development): each item pins, the next covers it.
document.addEventListener('DOMContentLoaded', () => {
  const stacks = [...document.querySelectorAll('[data-stack]')];
  if (!stacks.length) return;
  const header = document.querySelector('.site-header');
  const hdrH = () => (header ? header.offsetHeight : 0);
  const setHdr = () => document.documentElement.style.setProperty('--hdr', hdrH() + 'px');
  setHdr();
  let ticking = false;
  const update = () => {
    const vh = window.innerHeight, hdr = hdrH();
    stacks.forEach(stack => {
      const items = [...stack.children];
      items.forEach((it, i) => {
        const next = items[i + 1];
        if (!next) return;
        const top = next.getBoundingClientRect().top;
        const p = Math.min(1, Math.max(0, 1 - (top - hdr) / (vh - hdr)));
        it.style.setProperty('--cover', p.toFixed(3));
      });
    });
    ticking = false;
  };
  window.addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  window.addEventListener('resize', () => { setHdr(); update(); });
  update();
});

// Home: "Read more" pill follows the cursor over product images and text
document.addEventListener('DOMContentLoaded', () => {
  const targets = document.querySelectorAll('[data-peek]');
  if (!targets.length || !window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  const pill = document.createElement('div');
  pill.className = 'peek-pill'; pill.textContent = 'Read more';
  const label = t => (t.dataset.peek && t.dataset.peek.length) ? t.dataset.peek : 'Read more'; pill.setAttribute('aria-hidden', 'true');
  document.body.appendChild(pill);
  let x = 0, y = 0, cx = 0, cy = 0, raf = null;
  const still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const tick = () => {
    cx += (x - cx) * (still ? 1 : .22); cy += (y - cy) * (still ? 1 : .22);
    pill.style.left = cx + 'px'; pill.style.top = cy + 'px';
    raf = requestAnimationFrame(tick);
  };
  targets.forEach(t => {
    t.addEventListener('mouseenter', e => {
      pill.textContent = label(t);
      if (!pill.classList.contains('on')) { cx = x = e.clientX; cy = y = e.clientY; }
      pill.classList.add('on');
      if (!raf) raf = requestAnimationFrame(tick);
    });
    t.addEventListener('mousemove', e => { x = e.clientX; y = e.clientY; pill.classList.add('on'); if (!raf) raf = requestAnimationFrame(tick); });
    t.addEventListener('mouseleave', () => { pill.classList.remove('on'); cancelAnimationFrame(raf); raf = null; });
  });
  window.addEventListener('scroll', () => pill.classList.remove('on'), { passive: true });
});

// YouTube: play inline on the live site; open YouTube when viewing local files
document.addEventListener('click', e => {
  const a = e.target.closest('.yt[data-yt]');
  if (!a || location.protocol === 'file:') return;
  e.preventDefault();
  const f = document.createElement('iframe');
  f.src = `https://www.youtube.com/embed/${a.dataset.yt}?autoplay=1&rel=0`;
  f.title = a.getAttribute('aria-label') || 'Video';
  f.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture';
  f.referrerPolicy = 'strict-origin-when-cross-origin';
  f.allowFullscreen = true;
  a.replaceWith(Object.assign(document.createElement('div'), { className: 'yt' }));
  document.querySelector('div.yt:empty').appendChild(f);
});
