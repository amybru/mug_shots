/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("mainnav").style.top = "0";
  } else {
    document.getElementById("mainnav").style.top = "-50px";
  }
  prevScrollpos = currentScrollPos;
}


/* Side Nav, comes on small screens */
/* Set the width of the side navigation to 250px */
function openNav() {
  document.getElementById("side-nav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
  document.getElementById("side-nav").style.width = "0";
}