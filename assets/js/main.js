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
     1. Global navigation
     One controller drives both presentations:
       desktop (>860px) — dropdown panels opened by hover, click or keyboard
       mobile  (<=860px) — a slide-in drawer whose panels behave as accordions
     `aria-expanded` on the trigger is the single source of truth in both.
     ------------------------------------------------------------------------- */
  var MOBILE = '(max-width: 860px)';

  function onMediaChange(mq, fn) {
    if (mq.addEventListener) mq.addEventListener('change', fn);
    else if (mq.addListener) mq.addListener(fn);
  }

  function initNav() {
    var header = document.querySelector('[data-header]');
    var toggle = document.querySelector('[data-nav-toggle]');
    var drawer = document.querySelector('[data-nav-panel]');
    if (!header || !toggle || !drawer) return;

    var groups = Array.prototype.slice.call(document.querySelectorAll('[data-nav-group]'))
      .map(function (group) {
        var trigger = group.querySelector('.nav__trigger');
        var panel = trigger && document.getElementById(trigger.getAttribute('aria-controls'));
        return trigger && panel ? { group: group, trigger: trigger, panel: panel } : null;
      })
      .filter(Boolean);

    var mobile = window.matchMedia(MOBILE);
    var scrollY = 0;
    var hoverTimer = null;

    /* -- the drawer needs to start below the header, whatever height it is -- */
    function measureHeader() {
      var bar = header.querySelector('.header-top');
      if (bar) {
        document.documentElement.style.setProperty(
          '--header-h', Math.round(bar.getBoundingClientRect().height) + 'px');
      }
    }

    /* -- dropdown / accordion -------------------------------------------- */
    function setPanel(entry, open) {
      entry.trigger.setAttribute('aria-expanded', String(open));
      entry.panel.hidden = !open;
    }

    function closeAllPanels(except) {
      groups.forEach(function (entry) {
        if (entry !== except) setPanel(entry, false);
      });
    }

    groups.forEach(function (entry) {
      entry.trigger.addEventListener('click', function () {
        var open = entry.trigger.getAttribute('aria-expanded') === 'true';

        // On a mouse, hovering the trigger has already opened the panel by the
        // time the click lands. Toggling here would shut it the instant the
        // visitor clicked the thing they wanted, so the first click only makes
        // the open state deliberate; a second one closes it.
        if (open && entry.hoverOpened) {
          entry.hoverOpened = false;
          return;
        }

        if (!mobile.matches) closeAllPanels(entry);
        setPanel(entry, !open);
        entry.hoverOpened = false;
      });

      // Pointer affordance is desktop-only; touch fires click instead.
      entry.group.addEventListener('mouseenter', function () {
        if (mobile.matches) return;
        window.clearTimeout(hoverTimer);
        closeAllPanels(entry);
        setPanel(entry, true);
        entry.hoverOpened = true;
      });
      entry.group.addEventListener('mouseleave', function () {
        if (mobile.matches) return;
        hoverTimer = window.setTimeout(function () {
          setPanel(entry, false);
          entry.hoverOpened = false;
        }, 120);
      });

      // Tabbing out of the group closes it, so focus never lands behind a panel.
      entry.group.addEventListener('focusout', function (e) {
        if (mobile.matches) return;
        if (!entry.group.contains(e.relatedTarget)) setPanel(entry, false);
      });
    });

    /* -- body scroll lock -------------------------------------------------
       position:fixed rather than overflow:hidden, because iOS Safari ignores
       overflow on <body> and scrolls the page behind the drawer anyway. */
    function lockScroll() {
      scrollY = window.pageYOffset || document.documentElement.scrollTop;
      document.body.style.top = '-' + scrollY + 'px';
      document.body.classList.add('is-nav-locked');
    }
    function unlockScroll() {
      document.body.classList.remove('is-nav-locked');
      document.body.style.top = '';
      // `scroll-behavior: smooth` would animate the restore and leave the
      // visitor watching the page fly back to where they already were.
      var root = document.documentElement;
      var previous = root.style.scrollBehavior;
      root.style.scrollBehavior = 'auto';
      window.scrollTo(0, scrollY);
      root.style.scrollBehavior = previous;
    }

    /* -- drawer ------------------------------------------------------------ */
    function drawerOpen() { return toggle.getAttribute('aria-expanded') === 'true'; }

    function setDrawer(open) {
      if (open === drawerOpen()) return;
      toggle.setAttribute('aria-expanded', String(open));
      drawer.classList.toggle('is-open', open);
      if (open) {
        measureHeader();
        lockScroll();
      } else {
        unlockScroll();
        closeAllPanels();
      }
    }

    toggle.addEventListener('click', function () { setDrawer(!drawerOpen()); });

    // Choosing a destination dismisses whatever is open.
    drawer.addEventListener('click', function (e) {
      var link = e.target.closest && e.target.closest('a');
      if (!link) return;
      if (mobile.matches) setDrawer(false);
      else closeAllPanels();
    });

    /* -- global dismissal -------------------------------------------------- */
    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape' && e.key !== 'Esc') return;
      var openPanel = groups.filter(function (entry) {
        return entry.trigger.getAttribute('aria-expanded') === 'true';
      })[0];

      if (openPanel && !mobile.matches) {
        setPanel(openPanel, false);
        openPanel.trigger.focus();
      } else if (drawerOpen()) {
        setDrawer(false);
        toggle.focus();
      } else if (openPanel) {
        setPanel(openPanel, false);
      }
    });

    document.addEventListener('click', function (e) {
      if (mobile.matches || header.contains(e.target)) return;
      closeAllPanels();
    });

    /* -- focus trap, drawer only ------------------------------------------- */
    var FOCUSABLE = 'a[href], button:not([disabled]), input, select, textarea, [tabindex]:not([tabindex="-1"])';
    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab' || !drawerOpen() || !mobile.matches) return;
      var items = Array.prototype.slice.call(header.querySelectorAll(FOCUSABLE))
        .filter(function (el) { return el.offsetParent !== null || el === document.activeElement; });
      if (!items.length) return;
      var first = items[0];
      var last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault(); last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault(); first.focus();
      }
    });

    /* -- crossing the breakpoint must never strand an open overlay --------- */
    onMediaChange(mobile, function () {
      setDrawer(false);
      closeAllPanels();
      measureHeader();
    });

    var resizeTimer = null;
    window.addEventListener('resize', function () {
      window.clearTimeout(resizeTimer);
      resizeTimer = window.setTimeout(measureHeader, 120);
    });

    measureHeader();
  }

  /* ---------------------------------------------------------------------------
     2. Current-page marking
     Pages declare themselves with <body data-page="services">; the shared header
     partial stays byte-identical everywhere.
     ------------------------------------------------------------------------- */
  function initCurrentPage() {
    var page = document.body.getAttribute('data-page');
    if (page) {
      var item = document.querySelector('[data-nav="' + page + '"]');
      if (item) item.setAttribute('aria-current', 'page');
    }

    // Mark the exact destination inside dropdown panels and the footer.
    // Hrefs are authored root-absolute but ship relative (`../../services/…`)
    // so the site works at any mount point, so a string comparison against
    // location.pathname never matches. Resolve each href against the document
    // first — that also keeps this correct under a subpath deployment.
    var here = window.location.pathname.replace(/index\.html$/, '');
    var links = document.querySelectorAll('.nav__panelList a, .footer-links a');
    Array.prototype.forEach.call(links, function (a) {
      var href = a.getAttribute('href');
      if (!href || /^(https?:|mailto:|tel:|#)/.test(href)) return;
      var path;
      try {
        path = new URL(href, window.location.href).pathname.replace(/index\.html$/, '');
      } catch (e) {
        return;
      }
      if (path === here) a.setAttribute('aria-current', 'page');
    });
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

    // Only now does the CSS hide anything. Everything above this line leaves the
    // page fully visible, so a failed script can never blank the content.
    document.documentElement.classList.add('reveal-on');

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
     4. Forms
     One controller for every form on the site. A form opts in with
     `data-arco-form` and declares its own wiring in markup, so adding a form
     never means editing this file.

     ┌── CONFIGURING A REAL BACKEND ─────────────────────────────────────────┐
     │ Every form here posts JSON to whatever URL sits in `data-endpoint`.    │
     │ That attribute is EMPTY on all three forms today, so nothing is sent   │
     │ anywhere — the visitor is handed a pre-filled mail draft instead.      │
     │                                                                        │
     │ To connect a provider (Formspree, Basin, Netlify Forms, a serverless   │
     │ function — anything that accepts a JSON POST and answers 2xx):         │
     │                                                                        │
     │   1. Create the endpoint with the provider.                            │
     │   2. Put its URL in `data-endpoint` on the form element:                │
     │        data-endpoint="https://formspree.io/f/xxxxxxxx"                  │
     │      Forms live at: /get-a-quote/, /contact-us/, and the homepage       │
     │      consultation section (#quote-form).                               │
     │   3. Nothing else changes. This file already POSTs, handles failure,    │
     │      and only shows the success panel on a 2xx response.                │
     │                                                                        │
     │ A form endpoint URL is a public destination, not a secret. Never put    │
     │ an API key, token or password in the markup or in this file — anything  │
     │ that must stay private belongs behind a serverless function.            │
     └───────────────────────────────────────────────────────────────────────┘

     Markup contract:
       form[data-arco-form]      the form itself
         data-endpoint           POST target; empty = mail-draft fallback
         data-fallback-email     address used by the fallback
         data-subject            subject line for the fallback draft
         data-success            selector for the success panel (starts hidden)
         data-status             selector for the polite status region
       field[data-validate=…]    one of: text | name | phone | email | zip | choice
         data-error              optional custom message
         id + <span id="<id>-error"> for the inline message
       [data-honeypot]           off-screen field a human never fills
       [data-form-reset]         optional "send another" button in the panel
     ------------------------------------------------------------------------- */
  var VALIDATORS = {
    text: {
      test: function (v) { return v.trim().length > 0; },
      message: 'This field is required.'
    },
    name: {
      test: function (v) { return v.trim().length >= 2; },
      message: 'Please enter your name.'
    },
    phone: {
      test: function (v) { return v.replace(/\D/g, '').length >= 10; },
      message: 'Please enter a phone number with at least 10 digits.'
    },
    email: {
      test: function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()); },
      message: 'Please enter a valid email address.'
    },
    zip: {
      test: function (v) { return /^\d{5}(-\d{4})?$/.test(v.trim()); },
      message: 'Please enter a 5-digit ZIP code.'
    },
    choice: {
      test: function (v) { return v.trim().length > 0; },
      message: 'Please choose an option.'
    }
  };

  function initForms() {
    var forms = Array.prototype.slice.call(document.querySelectorAll('form[data-arco-form]'));
    forms.forEach(setUpForm);
  }

  function setUpForm(form) {
    var success = document.querySelector(form.getAttribute('data-success') || '');
    var status = document.querySelector(form.getAttribute('data-status') || '');
    if (!success || !status) return;

    var fields = Array.prototype.slice.call(form.querySelectorAll('[data-validate]'));
    var honeypot = form.querySelector('[data-honeypot]');
    var button = form.querySelector('button[type="submit"]');

    function ruleFor(field) {
      return VALIDATORS[field.getAttribute('data-validate')] || VALIDATORS.text;
    }

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
      var count = 0;
      fields.forEach(function (field) {
        var ok = ruleFor(field).test(field.value);
        setError(field, ok ? '' : (field.getAttribute('data-error') || ruleFor(field).message));
        if (!ok) { count++; if (!firstBad) firstBad = field; }
      });
      return { first: firstBad, count: count };
    }

    // Clear a field's error the moment it becomes valid again.
    fields.forEach(function (field) {
      var clear = function () {
        if (field.getAttribute('aria-invalid') === 'true' && ruleFor(field).test(field.value)) {
          setError(field, '');
        }
      };
      field.addEventListener('input', clear);
      field.addEventListener('change', clear);
    });

    function showSuccess() {
      form.hidden = true;
      success.hidden = false;
      var heading = success.querySelector('[data-form-success-heading]') || success.querySelector('h2, h3');
      if (heading) {
        if (!heading.hasAttribute('tabindex')) heading.setAttribute('tabindex', '-1');
        heading.focus();
      }
    }

    // Every named control except the honeypot, in document order.
    function collect() {
      var out = [];
      Array.prototype.slice.call(form.elements).forEach(function (el) {
        if (!el.name || el.disabled) return;
        if (honeypot && el === honeypot) return;
        if ((el.type === 'radio' || el.type === 'checkbox') && !el.checked) return;
        var label = el.getAttribute('data-label') || el.name;
        out.push({ key: el.name, label: label, value: el.value });
      });
      return out;
    }

    function payload(pairs) {
      var obj = {};
      pairs.forEach(function (p) { obj[p.key] = p.value; });
      return obj;
    }

    function mailtoFallback(pairs) {
      var address = form.getAttribute('data-fallback-email');
      if (!address) {
        status.textContent =
          'This form is not connected yet. Please call 305-951-8862 or email ' +
          'jonah@arcooutdoors.com and we will pick it up right away.';
        return;
      }
      var body = pairs.map(function (p) { return p.label + ': ' + (p.value || '(not given)'); }).join('\n');
      status.textContent = 'Opening your email app so you can send this…';
      window.location.href = 'mailto:' + address +
        '?subject=' + encodeURIComponent(form.getAttribute('data-subject') || 'Website enquiry') +
        '&body=' + encodeURIComponent(body);
      window.setTimeout(showSuccess, 900);
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      // A real visitor never fills a field they cannot see.
      if (honeypot && honeypot.value) { showSuccess(); return; }

      var result = validate();
      if (result.first) {
        status.textContent = result.count === 1
          ? 'One field needs attention — see the highlighted message below.'
          : 'Please correct the ' + result.count + ' highlighted fields.';
        result.first.focus();
        return;
      }

      var pairs = collect();
      var endpoint = form.getAttribute('data-endpoint');
      if (!endpoint) { mailtoFallback(pairs); return; }

      if (button) button.disabled = true;
      status.textContent = 'Sending…';

      fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(payload(pairs))
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

    var resetBtn = success.querySelector('[data-form-reset]');
    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        form.reset();
        fields.forEach(function (field) { setError(field, ''); });
        if (button) button.disabled = false;
        status.textContent = '';
        success.hidden = true;
        form.hidden = false;
        var first = form.querySelector('[data-validate]');
        if (first) first.focus();
      });
    }
  }

  /* ---------------------------------------------------------------------------
     5. Tag filter
     Filters a grid of [data-tags] items from a row of [data-filter] buttons.
     Generic: any page can mark up a [data-filter-root] region and get this.

     Like initReveal, the CSS keeps every item visible until this function has
     actually run — `.filter-on` is added below, and the filter bar is hidden
     without it. A script that fails to load therefore leaves a complete,
     readable list rather than a control that does nothing.
     ------------------------------------------------------------------------- */
  function initFilter() {
    var roots = document.querySelectorAll('[data-filter-root]');
    if (!roots.length) return;

    Array.prototype.forEach.call(roots, function (root) {
      var chips = Array.prototype.slice.call(root.querySelectorAll('[data-filter]'));
      var items = Array.prototype.slice.call(root.querySelectorAll('[data-tags]'));
      if (!chips.length || !items.length) return;

      var status = root.querySelector('[data-filter-status]');
      var empty = root.querySelector('[data-filter-empty]');
      var reset = root.querySelector('[data-filter-reset]');
      var total = items.length;

      function label(key) {
        for (var i = 0; i < chips.length; i++) {
          if (chips[i].getAttribute('data-filter') === key) {
            return (chips[i].textContent || '').replace(/\s+\d+\s*$/, '').trim();
          }
        }
        return key;
      }

      function apply(key, announce) {
        var shown = 0;

        items.forEach(function (item) {
          var tags = ' ' + (item.getAttribute('data-tags') || '') + ' ';
          var match = key === 'all' || tags.indexOf(' ' + key + ' ') > -1;
          item.hidden = !match;
          if (match) shown += 1;
        });

        chips.forEach(function (chip) {
          chip.setAttribute('aria-pressed', chip.getAttribute('data-filter') === key ? 'true' : 'false');
        });

        if (empty) empty.hidden = shown !== 0;

        // Left empty until the visitor filters something, so the live region
        // does not announce a count nobody asked for on page load.
        if (status && announce) {
          status.textContent = key === 'all'
            ? 'Showing all ' + total + ' entries'
            : 'Showing ' + shown + ' of ' + total + ' — ' + label(key);
        }
      }

      chips.forEach(function (chip) {
        chip.addEventListener('click', function () {
          apply(chip.getAttribute('data-filter'), true);
        });
      });

      if (reset) {
        reset.addEventListener('click', function () {
          apply('all', true);
          var first = chips[0];
          if (first) first.focus();
        });
      }

      document.documentElement.classList.add('filter-on');
      apply('all', false);
    });
  }

  /* ---------------------------------------------------------------------------
     6. Footer year
     ------------------------------------------------------------------------- */
  function initYear() {
    var els = document.querySelectorAll('[data-year]');
    Array.prototype.forEach.call(els, function (el) {
      el.textContent = String(new Date().getFullYear());
    });
  }

  function init() {
    initNav();
    initCurrentPage();
    initReveal();
    initForms();
    initFilter();
    initYear();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
