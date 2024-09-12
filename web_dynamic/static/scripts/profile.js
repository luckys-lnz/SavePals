document.addEventListener("DOMContentLoaded", () => {
  const user_id = sessionStorage.getItem("user_id");

  if (!user_id) {
    console.error("User ID not found");
    return;
  }

  // Fetch profile data when the page loads
  getProfile(user_id);

  // Ensure the form element exists before attaching event listener
  const profileForm = document.querySelector(".profile-form");
  if (profileForm) {
    profileForm.addEventListener("submit", async (event) => {
      event.preventDefault();

      const formData = new FormData(event.target);
      const data = {};
      formData.forEach((value, key) => {
        data[key] = value;
      });

      try {
        const response = await fetch(
          `http://127.0.0.1:5001/api/v1/users/${user_id}`,
          {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
          }
        );

        if (!response.ok) {
          throw new Error(`Failed to update profile: ${response.status}`);
        }

        // Log the user out and redirect to login
        sessionStorage.removeItem("user_id");
        window.location.href = "/signup";
      } catch (error) {
        console.error("Error updating profile:", error.message);
      }
    });
  } else {
    console.error("Profile form not found.");
  }
});

async function getProfile(user_id) {
  const url = `http://127.0.0.1:5001/api/v1/users/${user_id}`;

  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`Failed to fetch user profile: ${response.status}`);
    }

    const json = await response.json();
    document.getElementById("first-name").value = json.first_name || "";
    document.getElementById("last-name").value = json.last_name || "";
    document.getElementById("email").value = json.email || "";
    document.getElementById("age").value = json.age || "";
    document.getElementById("phone").value = json.phone || "";
  } catch (error) {
    console.error("Error fetching profile:", error.message);
  }
}
