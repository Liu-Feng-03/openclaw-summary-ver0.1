
const currentPath = window.location.pathname.replace(/index\.html$/, '/');
document.querySelectorAll('[data-nav]').forEach((link) => {
  const href = link.getAttribute('href');
  const abs = new URL(href, window.location.href).pathname.replace(/index\.html$/, '/');
  if (abs === currentPath || (abs !== '/' && currentPath.startsWith(abs))) link.classList.add('active');
});
