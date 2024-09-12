$(document).ready(function() {
    // Retrieve the value of 'user_id' from sessionStorage
    const userId = sessionStorage.getItem('user_id');

    $.ajax({
        url: `http://127.0.0.1:5001/api/v1/users/${userId}/groups`,
        method: 'GET',
        success: function(groups) {
            // Clear existing content
            $('#list-friends').empty();

            // Handle case where the user is not part of any group
            if (groups.length === 0) {
                $('#list-friends').text("No friends found");
                return;
            }

            // Retrieve users in each group
            let usersList = new Set();
            groups.forEach(group => {
                group.users.forEach(user => {
                    usersList.add(user);
                });
            });

            // Convert users list to an array
            let friends = Array.from(usersList);

            // Add each friend to the list
            friends.forEach(friend => {
                $('#list-friends').append(`
                    <li>
                        <span>${friend.first_name}</span>
                        <span>${friend.last_name}</span>
                        <span>${friend.email}</span>
                        <span>${friend.phone}</span>
                    </li>
                `);
            });
        },
        error: function(xhr, status, error) {
            console.error('Failed to load groups:', status, error);
            $('#list-friends').text("Failed to load friends. Please try again later.");
        }
    });
});
