const btnOpen = document.querySelector("#open-mobile-menu");
if (btnOpen) {
  btnOpen.addEventListener("click", () => {
    const mobileMenu = document.querySelector("#mobile-menu");
    if (mobileMenu) {
      mobileMenu.setAttribute("aria-expanded", "true");
    }
  });
}
const btnClose = document.querySelector("#close-mobile-menu");
if (btnClose) {
  btnClose.addEventListener("click", () => {
    const mobileMenu = document.querySelector("#mobile-menu");
    if (mobileMenu) {
      mobileMenu.setAttribute("aria-expanded", "false");
    }
  });
}
