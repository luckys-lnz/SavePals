document.addEventListener("DOMContentLoaded", () => {
  // Get the user ID from the URL
  const url = new URL(window.location.href);
  const user_id = sessionStorage.getItem("user_id");

  // Check if user_id is available
  if (!user_id) {
    console.error("User ID not found in the URL");
    return;
  }

  // Fetch profile from API
  getProfile(user_id);
});

// Fetch profile from API
async function getProfile(user_id) {
  const url = `http://127.0.0.1:5001/api/v1/users/${user_id}`;

  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });

    // Check if response is okay
    if (!response.ok) {
      throw new Error(`Failed to fetch user profile: ${response.status}`);
    }

    // Parse the response JSON
    const json = await response.json();
    console.log("API Response:", json);

    // Check if the required data exists
    if (!json || !json.first_name || !json.last_name || !json.email || !json.age || !json.phone) {
      console.error("Incomplete user data received");
      return;
    }

    // Populate the profile form with the fetched data
    document.getElementById("first-name").value = json.first_name || "";
    document.getElementById("last-name").value = json.last_name || "";
    document.getElementById("email").value = json.email || "";
    document.getElementById("age").value = json.age || "";
    document.getElementById("phone").value = json.phone || "";

    // For testing purpose
    console.log("User profile fetched successfully:", json);
  } catch (error) {
    console.error("Error fetching profile:", error.message);
  }
}

