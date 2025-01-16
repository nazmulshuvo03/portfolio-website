document.addEventListener("DOMContentLoaded", () => {
  const navbar = document.getElementById("navbar");
  const navItems = document.querySelectorAll(".nav-link");
  const sections = document.querySelectorAll("section");

  const navbarHeight = document.getElementById("navbar").offsetHeight;
  const navLinks = document.querySelectorAll(".nav-link");

  // setting initial classes
  navbar.classList.add("navbar-light", "bg-transparent", "border-0");
  navItems.forEach((item) => {
    item.classList.add("text-white");
  });

  // adding navbar size offsetTop for every section
  navLinks.forEach((link) => {
    link.addEventListener("click", function (event) {
      event.preventDefault();
      const targetId = this.getAttribute("href").substring(1);
      const targetSection = document.getElementById(targetId);

      if (targetSection) {
        const offsetTop = targetSection.offsetTop - navbarHeight;
        window.scrollTo({
          top: offsetTop,
          behavior: "smooth",
        });
      }
    });
  });

  // updating navbar classes depending on scroll
  window.addEventListener("scroll", () => {
    let currentSection = "";
    sections.forEach((section) => {
      const sectionTop = section.offsetTop - navbarHeight;
      const sectionHeight = section.offsetHeight;

      if (
        window.scrollY >= sectionTop &&
        window.scrollY < sectionTop + sectionHeight
      ) {
        currentSection = section.getAttribute("id");
      }
    });
    if (currentSection !== "hero") {
      navbar.classList.remove(
        "navbar-light",
        "bg-transparent",
        "text-white",
        "border-0",
      );
      navbar.classList.add("navbar-light", "bg-white", "shadow-sm", "border-2");
      navItems.forEach((item) => {
        item.classList.remove("text-white");
      });
    } else {
      navbar.classList.remove("bg-white", "shadow-sm", "border-2");
      navbar.classList.add("navbar-light", "bg-transparent", "border-0");
      navItems.forEach((item) => {
        item.classList.add("text-white");
      });
    }

    // Update active class on navbar links
    navItems.forEach((item) => {
      const link = item;
      if (link.getAttribute("href").substring(1) === currentSection) {
        item.classList.add("active");
      } else {
        item.classList.remove("active");
      }
    });
  });
});
