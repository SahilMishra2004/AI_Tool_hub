document.addEventListener("DOMContentLoaded", function () {
  const themeOptions = document.querySelectorAll(".theme-option");

  // Load previously saved theme
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme) {
    document.documentElement.setAttribute("data-bs-theme", savedTheme);
  }

  // Add event listeners to dropdown items
  themeOptions.forEach(option => {
    option.addEventListener("click", function (e) {
      e.preventDefault();
      const selectedTheme = this.getAttribute("data-theme");
      document.documentElement.setAttribute("data-bs-theme", selectedTheme);
      localStorage.setItem("theme", selectedTheme);
    });
  });
});
