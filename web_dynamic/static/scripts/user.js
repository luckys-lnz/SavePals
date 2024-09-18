$(document).ready(function() {
    // Retrieve the value of 'user_id' from sessionStorage
    const userId = sessionStorage.getItem('user_id');
    
    if (userId) {
        // Fetch the data from the API endpoint using AJAX
        $.ajax({
            type: "GET",
            url: `http://127.0.0.1:5001/api/v1/users/${userId}`, // Include userId in the URL
            success: function (user) {
                $("#user-first-name").text(`Hello, ${user.first_name}`); // Display user's first name
            },
            error: function (xhr, status, error) {
                console.error('Failed to fetch user data:', status, error);
                $("#user-first-name").text('Error loading user data'); // Handle error scenario
            }
        });
    } else {
        $("#user-first-name").text('User ID not found'); // Handle missing user ID scenario
    }
});
