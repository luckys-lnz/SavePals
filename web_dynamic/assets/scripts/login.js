$(document).ready(function() {
  $('#login-form').on('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Capture the form data
    const email = $('#login-email').val();
    const password = $('#login-password').val();

    // Send the data to the API endpoint using AJAX
    $.ajax({
      url: 'https://127.0.0.1:5000/api/v1/login',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({
        email: email,
        password: password
      }),
      success: function(response) {
        // Store the JWT token in local storage
        sessionStorage.setItem('token', response.token);
		sessionStorage.setItem('user_id', response.user_id);
		
        $('#signup-success').text('Login successful, Redirecting to dashboard...');
		
		// Redirect to the dashboard after a short delay (optional)
        setTimeout(function() {
          window.location.href = '/dashboard'; //dashboard URL
        }, 1000); // 1-second delay

      },
      error: function(xhr, status, error) {
        $('#message').text('Error: ' + xhr.responseJSON.message);
      }
    });
  });
});



$(document).ready(function() {
    $('#logout-button').on('click', function() {
        logout();
    });
});

function logout() {
    // Remove token from sessionStorage
    sessionStorage.removeItem('token');
    
    // Optionally, you can also remove any other user-related data if needed
    sessionStorage.removeItem('user_id');
    
    // Redirect to the login page
    window.location.href = '/login';
}
