// Document ready function
document.addEventListener('DOMContentLoaded', function() {
  // Initialize flash messages with auto-dismiss
  initFlashMessages();
});

// Navigation toggle
function open_nav() {
  var navbar = document.getElementById("navbar");
  if (navbar.className === "closed") {
    navbar.className = "open";
  } else {
    navbar.className = "closed";
  }
}

// Form submission helper
function submit_form() {
  this.closest("form").submit();
}

// Add link fields in wishlist forms
function addLinkField() {
  const container = document.getElementById('links-container');
  const newLinkItem = document.createElement('div');
  newLinkItem.className = 'link-item';

  const urlInput = document.createElement('input');
  urlInput.type = 'text';
  urlInput.name = 'link_urls';
  urlInput.placeholder = 'Link URL';

  const descInput = document.createElement('input');
  descInput.type = 'text';
  descInput.name = 'link_descs';
  descInput.placeholder = 'Link Description';

  newLinkItem.appendChild(urlInput);
  newLinkItem.appendChild(descInput);
  container.appendChild(newLinkItem);

  // Add smooth animation
  newLinkItem.style.opacity = '0';
  newLinkItem.style.transform = 'translateY(10px)';
  newLinkItem.style.transition = 'opacity 0.3s ease, transform 0.3s ease';

  // Trigger reflow to ensure transition works
  void newLinkItem.offsetWidth;

  newLinkItem.style.opacity = '1';
  newLinkItem.style.transform = 'translateY(0)';

  // Focus on the new URL input field
  urlInput.focus();
}

// Initialize flash messages with auto-dismiss
function initFlashMessages() {
  const flashMessages = document.querySelectorAll('.flash');

  flashMessages.forEach(function(message) {
    // Add close button
    const closeButton = document.createElement('span');
    closeButton.innerHTML = '&times;';
    closeButton.className = 'flash-close';
    closeButton.style.float = 'right';
    closeButton.style.cursor = 'pointer';
    closeButton.style.fontWeight = 'bold';
    closeButton.style.marginLeft = '10px';

    closeButton.addEventListener('click', function() {
      dismissFlashMessage(message);
    });

    message.insertBefore(closeButton, message.firstChild);

    // Auto-dismiss after 5 seconds (except for errors)
    if (!message.classList.contains('flash-error')) {
      setTimeout(function() {
        dismissFlashMessage(message);
      }, 5000);
    }
  });
}

// Dismiss a flash message with animation
function dismissFlashMessage(message) {
  message.style.opacity = '0';
  message.style.transform = 'translateY(-10px)';

  setTimeout(function() {
    message.style.display = 'none';
  }, 300);
}
