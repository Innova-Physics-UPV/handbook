(() => {
  // A link back to the website in the top bar, before mdBook's own buttons
  // (print, the repository, suggest an edit).
  const buttons = document.querySelector('#mdbook-menu-bar .right-buttons');
  if (buttons && !buttons.querySelector('.innova-home')) {
    const link = document.createElement('a');
    link.className = 'innova-home';
    link.href = 'https://innova-physics-upv.github.io/';
    link.title = 'Innova Physics UPV, the website';
    link.textContent = 'Website';
    buttons.prepend(link);
  }

  // mdBook 0.5's sidebar toggle is a <label> carrying button attributes,
  // which a label may not have, and the keyboard cannot reach it. Make it a
  // button for assistive technology and the keyboard: Enter and Space press
  // it, and mdBook's own click handling does the rest.
  const toggle = document.getElementById('mdbook-sidebar-toggle');
  if (toggle && !toggle.hasAttribute('role')) {
    toggle.setAttribute('role', 'button');
    toggle.tabIndex = 0;
    toggle.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        toggle.click();
      }
    });
  }
})();
