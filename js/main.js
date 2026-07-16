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
