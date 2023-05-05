document.addEventListener('DOMContentLoaded', function () {
  // Code to highlight and activate currently selected navigation bar option
  const currentPathArray = window.location.pathname.split('/');
  const currentPage = currentPathArray.pop();

  const navLinks = document.querySelectorAll('.nav-bar li a');
  navLinks.forEach(function (navLink) {
    const navLinkPathArray = navLink.getAttribute('href').split('/');
    const navLinkPage = navLinkPathArray.pop();
    if (navLinkPage === currentPage) {
      navLink.parentNode.classList.add('active');
    }
  });
});
