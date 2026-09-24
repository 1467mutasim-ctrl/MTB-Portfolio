'use strict';

const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('.navigation');
const closeMenu = () => { menuButton.setAttribute('aria-expanded', 'false'); navigation.classList.remove('is-open'); };
menuButton.addEventListener('click', () => {
  const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!isOpen));
  navigation.classList.toggle('is-open', !isOpen);
});
navigation.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });

const lightbox = document.querySelector('.lightbox');
const lightboxImage = lightbox.querySelector('.lightbox-image');
const lightboxCaption = document.querySelector('#lightbox-caption');
let lastTrigger = null;
document.querySelectorAll('[data-lightbox]').forEach(trigger => trigger.addEventListener('click', () => {
  lastTrigger = trigger;
  lightboxImage.src = trigger.dataset.lightbox;
  lightboxImage.alt = trigger.querySelector('img').alt;
  lightboxCaption.textContent = trigger.dataset.caption;
  lightbox.showModal();
  document.body.classList.add('dialog-open');
}));
lightbox.querySelector('.lightbox-close').addEventListener('click', () => lightbox.close());
lightbox.addEventListener('click', event => { if (event.target === lightbox) lightbox.close(); });
lightbox.addEventListener('close', () => { document.body.classList.remove('dialog-open'); lastTrigger?.focus(); });
