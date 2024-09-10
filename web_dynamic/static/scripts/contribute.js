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


// Handles select round filter
$(document).ready(function () {
    // Retrieve the value of 'group_id' from the plan select filter
    const groupId = $("select:first").val();
  
    $.ajax({
      url: `http://127.0.0.1:5001/api/v1/groups/${groupId}/rounds`,
      method: "GET",
      dataType: "json",
      success: function (rounds) {
        // Populate the select element with fetched data
        const $select = $("#round-select");
        $select.empty(); // Clear any existing options
  
        // Iterate through the fetched rounds data and append options
        rounds.forEach((round) => {
          $select.append(`
                      <option value="${round.id}">
                          ${round.round_number}
                      </option>
                  `);
        });
      },
      error: function (xhr, status, error) {
        console.error("Failed to fetch data:", error);
      },
    });
});


// Handles the contribute form
$(document).ready(function () {
    $("#contribute-form").on("submit", function (event) {
      event.preventDefault(); // Prevent the default form submission
  
      // Retrieve the value of 'user_id' from sessionStorage
      const userId = sessionStorage.getItem("user_id");

      // Capture the form data
      const amount = $("#amount").val();
      const group_id = $("#plan-select").val();
      const user_id = userId;
      const round_id = $("#round-select").val();
      
      // Send the data to the API endpoint using AJAX
      $.ajax({
        type: "POST",
        url: `http://127.0.0.1:5001/api/v1/groups`,
        contentType: "application/json",
        data: JSON.stringify({
          amount: amount,
          user_id: user_id,
          group_id: group_id,
          round_id: round_id,
        }),
        success: function (response) {
          $("#contribute-success").text("Contributed successfully!"); // Display success message
        },
        error: function (xhr, status, error) {
          $("#contribute-error").text("Error: " + xhr.responseJSON.message); // Display error message
        },
      });
    });
});
  