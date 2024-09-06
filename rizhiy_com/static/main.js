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

function addLink() {
    const container = document.getElementById("links-container");
    const index = container.children.length;
    const linkItem = document.createElement("div");
    linkItem.className = "link-item";
    linkItem.innerHTML = `
        <input type="text" name="links[${index}][url]" placeholder="URL" required />
        <input type="text" name="links[${index}][desc]" placeholder="Description" />
        <button type="button" onclick="removeLink(this)">Remove</button>
    `;
    container.appendChild(linkItem);
}

function removeLink(button) {
    const linkItem = button.parentElement;
    linkItem.remove();
}
