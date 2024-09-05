document.addEventListener("DOMContentLoaded", () => {
    const signupForm = document.getElementById("signup-form");
    const loginForm = document.getElementById("login-form");

    signupForm.addEventListener("submit", function (event) {
      const firstName = document.getElementById("signup-first-name").value;
      const lastName = document.getElementById("signup-last-name").value;
      const age = document.getElementById("age").value;
      const email = document.getElementById("signup-email").value;
      const phone = document.getElementById("phone").value;
      const password = document.getElementById("signup-password").value;
      const errorDiv = document.getElementById("signup-error");
      const successDiv = document.getElementById("signup-success");
      errorDiv.textContent = ""; // Clear previous errors
      successDiv.textContent = ""; // Clear previous successes

      // Basic validation
      if (firstName.length < 2) {
        errorDiv.textContent = "First Name must be at least 2 characters.";
        event.preventDefault();
        return;
      }

      if (lastName.length < 2) {
        errorDiv.textContent = "Last Name must be at least 2 characters.";
        event.preventDefault();
        return;
      }

      if (age < 1 || age > 120) {
        errorDiv.textContent = "Please enter a valid age between 1 and 120.";
        event.preventDefault();
        return;
      }

      if (!validateEmail(email)) {
        errorDiv.textContent = "Please enter a valid email address.";
        event.preventDefault();
        return;
      }

      // Validate phone number format
      const phonePattern = /^\(\d{3}\) \d{3}-\d{4}$/;
      if (!phonePattern.test(phone)) {
        errorDiv.textContent = "Phone number must be in the format (123) 456-7890.";
        event.preventDefault();
        return;
      }

      if (password.length < 6) {
        errorDiv.textContent = "Password must be at least 6 characters long.";
        event.preventDefault();
        return;
      }

      successDiv.textContent = "Signup successful!";
    });

    loginForm.addEventListener("submit", function (event) {
      const email = document.getElementById("login-email").value;
      const password = document.getElementById("login-password").value;
      const errorDiv = document.getElementById("login-error");
      const successDiv = document.getElementById("login-success");
      errorDiv.textContent = ""; // Clear previous errors
      successDiv.textContent = ""; // Clear previous successes

      // Basic validation
      if (!validateEmail(email)) {
        errorDiv.textContent = "Please enter a valid email address.";
        event.preventDefault();
        return;
      }

      if (password.length < 6) {
        errorDiv.textContent = "Password must be at least 6 characters long.";
        event.preventDefault();
        return;
      }

      successDiv.textContent = "Login successful!";
    });

    function validateEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(String(email).toLowerCase());
    }

    // Tab functionality
    window.openTab = function (evt, tabName) {
      // Get all elements with class="tabcontent"
      const tabcontent = document.getElementsByClassName("tabcontent");
      const tablinks = document.getElementsByClassName("tablinks");

      // Hide all tab content
      for (let i = 0; i < tabcontent.length; i++) {
        tabcontent[i].classList.remove("active");
      }

      // Remove "active" class from all tab links
      for (let i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("active");
      }

      // Add "active" class to the current tab and show the corresponding form
      document.getElementById(tabName).classList.add("active");
      evt.currentTarget.classList.add("active");
    };
  });
