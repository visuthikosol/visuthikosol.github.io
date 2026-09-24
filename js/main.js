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
  document.querySelectorAll('.pgrid img, .dev-media img, .final img, .split-media img, .logo-ring img, .bento img, .strip img, .pav img, .plans img, .final-set img, .idea-imgs img, .ch-set img, .models img, .sol-media img, .wide-fig img, .sol-extra img, .ortho2 img, .duo-media img').forEach(img => {
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

// About: words fill on hover/tap and show a caption; stats count up
document.addEventListener('DOMContentLoaded', () => {
  const words = document.querySelectorAll('.ab-word');
  const cap = document.querySelector('.ab-cap');
  if (words.length && cap) {
    const def = cap.textContent;
    const show = w => { words.forEach(x => x.classList.toggle('on', x === w)); cap.textContent = w.dataset.cap; cap.classList.add('live'); };
    const hide = () => { words.forEach(x => x.classList.remove('on')); cap.textContent = def; cap.classList.remove('live'); };
    const touch = window.matchMedia('(hover: none)').matches;
    words.forEach(w => {
      if (!touch) {
        w.addEventListener('mouseenter', () => show(w));
        w.addEventListener('focus', () => show(w));
        w.addEventListener('mouseleave', hide);
        w.addEventListener('blur', hide);
      }
      w.addEventListener('click', () => (touch && w.classList.contains('on') && cap.textContent === w.dataset.cap) ? hide() : show(w));
    });
    if (window.matchMedia('(hover: none)').matches) {
      
      // on touch, fill each word once as it comes into view
      let i = 0; words.forEach(w => setTimeout(() => w.classList.add('on'), 500 + 700 * i++));
      setTimeout(() => words.forEach(w => w.classList.remove('on')), 500 + 700 * words.length + 900);
    }
  }
  const nums = document.querySelectorAll('[data-count]');
  if (nums.length && 'IntersectionObserver' in window) {
    const still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (!e.isIntersecting) return; io.unobserve(e.target);
      const el = e.target, end = +el.dataset.count, suf = el.dataset.suffix || '';
      const start = end > 1000 ? end - 30 : 0, t0 = performance.now(), dur = still ? 0 : 1200;
      const step = t => { const p = dur ? Math.min(1, (t - t0) / dur) : 1; const v = Math.round(start + (end - start) * (1 - Math.pow(1 - p, 3))); el.textContent = v + (p === 1 ? suf : ''); if (p < 1) requestAnimationFrame(step); };
      requestAnimationFrame(step);
    }), { threshold: .6 });
    nums.forEach(n => io.observe(n));
  }
});

// Filmstrips: counter and arrows
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.strip-wrap').forEach(w => {
    const s = w.querySelector('.strip'), figs = [...s.children], out = w.querySelector('.strip-count');
    const btns = w.querySelectorAll('.sbtn');
    const idx = () => { let i = 0; figs.forEach((f, k) => { if (f.offsetLeft - s.offsetLeft <= s.scrollLeft + 8) i = k; }); if (s.scrollLeft + s.clientWidth >= s.scrollWidth - 4) i = figs.length - 1; return i; };
    const upd = () => { out.textContent = (idx() + 1) + ' / ' + figs.length; btns[0].disabled = s.scrollLeft <= 4; btns[1].disabled = s.scrollLeft + s.clientWidth >= s.scrollWidth - 4; };
    btns.forEach(b => b.addEventListener('click', () => { const i = Math.max(0, Math.min(figs.length - 1, idx() + +b.dataset.dir)); s.scrollTo({ left: figs[i].offsetLeft - s.offsetLeft, behavior: 'smooth' }); }));
    s.addEventListener('scroll', () => requestAnimationFrame(upd), { passive: true });
    figs.forEach(f => f.querySelector('img').addEventListener('load', upd));
    upd();
  });
});

// Mobile: turn multi-image rows into quiet auto cross-fades (no swipe hint needed)
document.addEventListener('DOMContentLoaded', () => {
  const mq = window.matchMedia('(max-width: 760px)');
  if (!mq.matches) return;
  const still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const sel = '.pgrid:not(.circles):not(.cols-1), .bento, .split.duo .split-media, .idea-imgs, .pv-pair, .plans, .final-set';
  document.querySelectorAll(sel).forEach(box => {
    const figs = [...box.children].filter(c => c.tagName === 'FIGURE');
    if (figs.length < 2) return;
    box.classList.add('fader');
    const dots = document.createElement('div'); dots.className = 'fader-dots';
    figs.forEach(() => dots.appendChild(document.createElement('i')));
    box.appendChild(dots);
    let i = 0, t = null;
    const show = n => { i = (n + figs.length) % figs.length; figs.forEach((f, k) => f.classList.toggle('on', k === i)); [...dots.children].forEach((d, k) => d.classList.toggle('on', k === i)); };
    show(0);
    if (still) return;
    const run = () => { clearInterval(t); t = setInterval(() => show(i + 1), 3200); };
    new IntersectionObserver(es => es.forEach(e => e.isIntersecting ? run() : clearInterval(t)), { threshold: .4 }).observe(box);
    let x0 = null;
    box.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; }, { passive: true });
    box.addEventListener('touchend', e => { if (x0 === null) return; const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) { show(i + (dx < 0 ? 1 : -1)); run(); } x0 = null; });
  });
});
