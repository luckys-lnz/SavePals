$(document).ready(function () {
    // Retrieve the value of 'user_id' from sessionStorage
    const userId = sessionStorage.getItem("user_id");
  
    $.ajax({
      url: `http://127.0.0.1:5001/api/v1/users/${userId}/groups`,
      method: "GET",
      dataType: "json",
      success: function (groups) {
        // Populate the select element with fetched data
        const $select = $("#plan-select");
        $select.empty(); // Clear any existing options
  
        // Iterate through the fetched groups data and append options
        groups.forEach((group) => {
          $select.append(`
                      <option value="${group.id}">
                          ${group.name}
                      </option>
                  `);
        });
      },
      error: function (xhr, status, error) {
        console.error("Failed to fetch data:", error);
      },
    });
});


// Handles the round form
$(document).ready(function () {
    $("#round-form").on("submit", function (event) {
      event.preventDefault(); // Prevent the default form submission

      // Capture the form data
      const round_number = $("#round-number").val();
      const group_id = $("#plan-select").val();
      const amount = $("#amount").val();
      
      // Send the data to the API endpoint using AJAX
      $.ajax({
        type: "POST",
        url: `http://127.0.0.1:5001/api/v1/groups/${group_id}/rounds`,
        contentType: "application/json",
        data: JSON.stringify({
          amount: amount,
          round_number: round_number,
          group_id: group_id,
        }),
        success: function (response) {
          $("#round-success").text("Round created successfully!"); // Display success message
        },
        error: function (xhr, status, error) {
          $("#round-error").text("Error: " + xhr.responseJSON.message); // Display error message
        },
      });
    });
});
