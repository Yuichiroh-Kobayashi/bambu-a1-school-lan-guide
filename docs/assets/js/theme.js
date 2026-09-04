/*
 * Theme control for the Bambu Lab A1 mini school LAN guide.
 *
 * Initial appearance follows the operating system preference through CSS only,
 * so the page renders correctly with JavaScript disabled. This script adds a
 * manual override for the current page view. Nothing is persisted: no
 * localStorage, no sessionStorage, no cookie, no IndexedDB. Reloading returns
 * the page to the system preference.
 */
(function () {
  "use strict";

  var root = document.documentElement;
  var toggle = document.querySelector("[data-theme-toggle]");
  if (!toggle) {
    return;
  }

  var buttons = toggle.querySelectorAll("[data-theme-value]");
  if (!buttons.length) {
    return;
  }

  function apply(mode) {
    if (mode === "light" || mode === "dark") {
      root.setAttribute("data-theme", mode);
    } else {
      root.removeAttribute("data-theme");
    }
    for (var i = 0; i < buttons.length; i += 1) {
      var pressed = buttons[i].getAttribute("data-theme-value") === mode;
      buttons[i].setAttribute("aria-pressed", pressed ? "true" : "false");
    }
  }

  for (var i = 0; i < buttons.length; i += 1) {
    buttons[i].addEventListener("click", function (event) {
      apply(event.currentTarget.getAttribute("data-theme-value"));
    });
  }

  apply("system");
  toggle.hidden = false;
})();
