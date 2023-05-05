document.addEventListener('DOMContentLoaded', function () {
  // Code to highlight and activate currently selected navigation bar option
  var currentPathArray = window.location.pathname.split('/');
  var currentPage = currentPathArray.pop();

  var navLinks = document.querySelectorAll('.navBar li a');
  navLinks.forEach(function (navLink) {
    var navLinkPathArray = navLink.getAttribute('href').split('/');
    var navLinkPage = navLinkPathArray.pop();
    if (navLinkPage === currentPage) {
      navLink.parentNode.classList.add('active');
    }
  });
});