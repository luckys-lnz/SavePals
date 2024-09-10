$(document).ready(function () {
    $("#create-plan-form").on("submit", function (event) {
      event.preventDefault(); // Prevent the default form submission
  
      // Retrieve the value of 'user_id' from sessionStorage
      const userId = sessionStorage.getItem("user_id");

      // Capture the form data
      const name = $("#goal-name").val();
      const number_members = $("#num-of-members").val();
      const target_amount = $("#target-amount").val();
      const description = $("#plan-description").val();
      const start_date = $("#start-date").val();
      const end_date = $("#end-date").val();
      const payment_intervals = $("#payment-interval").val();
      
      // Send the data to the API endpoint using AJAX
      $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5001/api/v1/groups",
        contentType: "application/json",
        data: JSON.stringify({
          name: name,
          description: description,
          target_amount: target_amount,
          number_members: number_members,
          start_date: start_date,
          end_date: end_date,
          payment_intervals: payment_intervals,
          creator_id: userId,
        }),
        success: function (response) {
          $("#plan-success").text("Plan created successfully!"); // Display success message
        },
        error: function (xhr, status, error) {
          $("#plan-error").text("Error: " + xhr.responseJSON.message); // Display error message
        },
      });
    });
  });
  