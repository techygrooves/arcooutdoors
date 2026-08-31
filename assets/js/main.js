/* =============================================================================
   Arco Outdoors — site behaviour
   Vanilla ES2018. No dependencies, no build step. Loaded with `defer`.
   Every feature is progressive: the page is fully usable with this file absent.
   ============================================================================= */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia
    ? window.matchMedia('(prefers-reduced-motion: reduce)')
    : { matches: false };

  /* ---------------------------------------------------------------------------
     1. Mobile navigation
     The button carries the state; CSS reads `aria-expanded` so the control and
     its visual affordance can never disagree.
     ------------------------------------------------------------------------- */
  function initNav() {
    var toggle = document.querySelector('.nav-toggle');
    var links = document.getElementById('primary-nav');
    if (!toggle || !links) return;

    function setOpen(open) {
      toggle.setAttribute('aria-expanded', String(open));
      links.classList.toggle('is-open', open);
    }

    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });

    // Choosing a destination closes the menu.
    links.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });

    // Returning to desktop width must not leave the menu latched open.
    var wide = window.matchMedia('(min-width: 861px)');
    var onChange = function (e) { if (e.matches) setOpen(false); };
    if (wide.addEventListener) wide.addEventListener('change', onChange);
    else if (wide.addListener) wide.addListener(onChange);
  }

  /* ---------------------------------------------------------------------------
     2. Current-section highlighting in the primary nav
     ------------------------------------------------------------------------- */
  function initNavHighlight() {
    if (!('IntersectionObserver' in window)) return;

    var links = Array.prototype.slice.call(
      document.querySelectorAll('#primary-nav a[href^="#"]')
    );
    if (!links.length) return;

    var map = {};
    var sections = [];
    links.forEach(function (a) {
      var id = a.getAttribute('href').slice(1);
      var el = id && document.getElementById(id);
      if (el) { map[id] = a; sections.push(el); }
    });
    if (!sections.length) return;

    var visible = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        visible[entry.target.id] = entry.isIntersecting;
      });
      var active = sections.filter(function (s) { return visible[s.id]; })[0];
      links.forEach(function (a) { a.removeAttribute('aria-current'); });
      if (active && map[active.id]) map[active.id].setAttribute('aria-current', 'page');
    }, { rootMargin: '-40% 0px -55% 0px' });

    sections.forEach(function (s) { io.observe(s); });
  }

  /* ---------------------------------------------------------------------------
     3. Scroll reveal — decorative only, and skipped entirely when the visitor
     has asked for reduced motion or the browser lacks IntersectionObserver.
     ------------------------------------------------------------------------- */
  function initReveal() {
    var items = Array.prototype.slice.call(document.querySelectorAll('.reveal'));
    if (!items.length) return;

    if (reduceMotion.matches || !('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-visible'); });
      return;
    }

    var io = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        obs.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.05 });

    items.forEach(function (el) { io.observe(el); });
  }

  /* ---------------------------------------------------------------------------
     4. Quote form
     Validates in place, then submits to `data-endpoint` when one is configured.
     With no endpoint the enquiry is handed to the visitor's mail client rather
     than being silently discarded.
     ------------------------------------------------------------------------- */
  function initForm() {
    var form = document.getElementById('quote-form');
    var success = document.getElementById('form-success');
    var status = document.getElementById('form-status');
    if (!form || !success || !status) return;

    var RULES = {
      'qf-name': {
        test: function (v) { return v.trim().length >= 2; },
        message: 'Please enter your name.'
      },
      'qf-phone': {
        test: function (v) { return (v.replace(/\D/g, '').length >= 10); },
        message: 'Please enter a phone number with at least 10 digits.'
      },
      'qf-email': {
        test: function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()); },
        message: 'Please enter a valid email address.'
      }
    };

    function setError(field, message) {
      var err = document.getElementById(field.id + '-error');
      if (message) {
        field.setAttribute('aria-invalid', 'true');
        if (err) err.textContent = message;
      } else {
        field.removeAttribute('aria-invalid');
        if (err) err.textContent = '';
      }
    }

    function validate() {
      var firstBad = null;
      Object.keys(RULES).forEach(function (id) {
        var field = document.getElementById(id);
        if (!field) return;
        var ok = RULES[id].test(field.value);
        setError(field, ok ? '' : RULES[id].message);
        if (!ok && !firstBad) firstBad = field;
      });
      return firstBad;
    }

    // Clear a field's error as soon as it becomes valid again.
    Object.keys(RULES).forEach(function (id) {
      var field = document.getElementById(id);
      if (!field) return;
      field.addEventListener('input', function () {
        if (field.getAttribute('aria-invalid') === 'true' && RULES[id].test(field.value)) {
          setError(field, '');
        }
      });
    });

    function showSuccess() {
      form.hidden = true;
      success.hidden = false;
      var heading = document.getElementById('form-success-heading');
      if (heading) heading.focus();
    }

    function mailtoFallback(data) {
      var subject = 'Consultation request — ' + (data.service || 'Arco Outdoors');
      var body = [
        'Name: ' + data.name,
        'Phone: ' + data.phone,
        'Email: ' + data.email,
        'Service of interest: ' + data.service,
        '',
        'Project details:',
        data.details || '(none provided)'
      ].join('\n');

      status.textContent = 'Opening your email app so you can send this request…';
      window.location.href = form.getAttribute('data-fallback-email')
        ? 'mailto:' + form.getAttribute('data-fallback-email') +
          '?subject=' + encodeURIComponent(subject) +
          '&body=' + encodeURIComponent(body)
        : '#';
      window.setTimeout(showSuccess, 900);
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      // Honeypot: a real visitor never fills a field they cannot see.
      var hp = document.getElementById('qf-company');
      if (hp && hp.value) { showSuccess(); return; }

      var firstBad = validate();
      if (firstBad) {
        status.textContent = 'Please correct the highlighted fields.';
        firstBad.focus();
        return;
      }

      var data = {
        name: (document.getElementById('qf-name') || {}).value || '',
        phone: (document.getElementById('qf-phone') || {}).value || '',
        email: (document.getElementById('qf-email') || {}).value || '',
        service: (document.getElementById('qf-service') || {}).value || '',
        details: (document.getElementById('qf-details') || {}).value || ''
      };

      var endpoint = form.getAttribute('data-endpoint');
      if (!endpoint) { mailtoFallback(data); return; }

      var button = form.querySelector('button[type="submit"]');
      if (button) { button.disabled = true; }
      status.textContent = 'Sending your request…';

      fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(data)
      }).then(function (res) {
        if (!res.ok) throw new Error('Request failed with status ' + res.status);
        status.textContent = '';
        showSuccess();
      }).catch(function () {
        status.textContent =
          'We could not send that automatically. Please call 305-951-8862 or ' +
          'email jonah@arcooutdoors.com and we will pick it up right away.';
        if (button) button.disabled = false;
      });
    });

    var resetBtn = document.getElementById('form-reset');
    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        form.reset();
        Object.keys(RULES).forEach(function (id) {
          var field = document.getElementById(id);
          if (field) setError(field, '');
        });
        var button = form.querySelector('button[type="submit"]');
        if (button) button.disabled = false;
        status.textContent = '';
        success.hidden = true;
        form.hidden = false;
        var first = document.getElementById('qf-name');
        if (first) first.focus();
      });
    }
  }

  /* ---------------------------------------------------------------------------
     5. Footer year
     ------------------------------------------------------------------------- */
  function initYear() {
    var el = document.getElementById('year');
    if (el) el.textContent = String(new Date().getFullYear());
  }

  function init() {
    initNav();
    initNavHighlight();
    initReveal();
    initForm();
    initYear();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
