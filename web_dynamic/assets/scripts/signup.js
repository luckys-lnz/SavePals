$(document).ready(function() {
  $('#signup-form').on('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Capture the form data
	const first_name = $('#signup-first-name').val()
	const last_name = $('#signup-last-name').val()
	const age = $('#age').val()
    const email = $('#signup-email').val();
	const phone = $('#phone').val()
    const password = $('#signup-password').val();

    // Send the data to the API endpoint using AJAX
    $.ajax({
      url: 'https://127.0.0.1:5000/api/v1/signup',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({
	    first_name: first_name,
		last_name: last_name,
		age: age,
		email: email,
        phone: phone,
        password: password
      }),
      success: function(response) {
        $('#signup-success').text(response.message); // Display success message
      },
      error: function(xhr, status, error) {
        $('#signup-error').text('Error: ' + xhr.responseJSON.message); // Display error message
      }
    });
  });
});
