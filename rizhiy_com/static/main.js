function open_nav() {
  var navbar = document.getElementById("navbar");
  if (navbar.className === "closed") {
    navbar.className = "open";
  } else {
    navbar.className = "closed";
  }
}

function submit_form() {
  this.closest("form").submit();
}

function addLinkField() {
    const container = document.getElementById('links-container');
    const newLinkItem = document.createElement('div');
    newLinkItem.className = 'link-item';
    newLinkItem.innerHTML = '<input type="text" name="link_urls" placeholder="Link URL" />' +
                            '<input type="text" name="link_descs" placeholder="Link Description" />';
    container.appendChild(newLinkItem);
}
