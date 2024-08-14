function open_nav() {
  var navbar = document.getElementById("navbar");
  if (navbar.className === "closed") {
    navbar.className = "open";
  } else {
    navbar.className = "closed";
  }
}
