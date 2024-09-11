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
      $select.append(`<option value=''>select plan</option>`)
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



$(document).ready(function () {
  // Function to load rounds based on the selected plan
  function loadRounds(groupId) {
      $.ajax({
          url: `http://127.0.0.1:5001/api/v1/groups/${groupId}/rounds`,
          method: "GET",
          dataType: "json",
          success: function (rounds) {
              // Populate the #round-select element with fetched data
              const $select = $("#round-select");
              $select.empty(); // Clear any existing options

              // Append a default option
              $select.append('<option value="">Select a Round</option>');

              // Iterate through the fetched rounds data and append options
              rounds.forEach((round) => {
                  $select.append(`
                      <option value="${round.id}">
                          Round ${round.round_number}
                      </option>
                  `);
              });
              console.log("dean")
          },
          error: function (xhr, status, error) {
              console.error("Failed to fetch data:", error);
          },
      });
  }

  // Event listener for when a plan is selected
  $("#plan-select").on("change", function () {
      const groupId = $(this).val(); // Get the selected group ID from #plan-select
      if (groupId) {
          loadRounds(groupId); // Load rounds for the selected group
      } else {
          // Clear rounds if no group is selected
          $("#round-select").empty().append('<option value="">Select a Round</option>');
      }
  });

  // Initial load of rounds if a plan is already selected
  const initialGroupId = $("#plan-select").val();
  if (initialGroupId) {
      loadRounds(initialGroupId);
  }
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
      url: `http://127.0.0.1:5001/api/v1/groups/${group_id}/rounds/${round_id}/users/${user_id}/contribution`,
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
