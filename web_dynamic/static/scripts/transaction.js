$(document).ready(function() {
    function loadTransactions() {
        const userFilter = $('select:first').val(); // Get selected user filter
        const planFiter = $('select:last').val(); // Get selected plan filter

        let apiUrl = '';
        // Retrieve the value of 'user_id' from sessionStorage
        const userId = sessionStorage.getItem('user_id');

        // Determine API URL based on filters
        if (userFilter && planFilter) {
            // If both filters are true, construct a URL that handles both
            apiUrl = `http://127.0.0.1:5001/api/v1/users/${userId}/groups/${planFiter}/transactions`;
        } else if (planFilter) {
            apiUrl = `http://127.0.0.1:5001/api/v1/groups/${planFilter}/transactions`;
        } else {
            apiUrl = `http://127.0.0.1:5001/api/v1/users/${userId}/transactions`;
        }

        $.ajax({
            url: apiUrl,
            method: 'GET',
            data: {
                user: userFilter,
                plan: planFilter
            },
            success: function(transactions) {
                // Clear existing transactions
                $('#list-transactions').empty();

                // Add each transaction to the list
                transactions.forEach(transaction => {
                $('#list-transactions').empty();
                $('').append(`
                        <li>
                            <span>${transaction.user.first_name}</span>
                            <span>${transaction.amount}</span>
                            <span>${transaction.group.name}</span>
                        </li>
                    `);
                });
            },
            error: function(xhr, status, error) {
                console.error('Failed to load transactions:', status, error);
            }
        });
    }

    // Load transactions on page load
    loadTransactions();

    // Reload transactions when filters change
    $('.filter select').on('change', function() {
        loadTransactions();
    });
});


$(document).ready(function() {

    // Retrieve the value of 'user_id' from sessionStorage
    const userId = sessionStorage.getItem('user_id');

    $.ajax({
        url: 'http://127.0.0.1:5001/api/v1/users/${userId}/groups',
        method: 'GET',
        dataType: 'json',
        success: function(groups) {
            // Populate the select element with fetched data
            const $select = $('#plan-select');
            $select.empty(); // Clear any existing options

            // Iterate through the fetched groups data and append options
            groups.forEach(group => {
                $select.append(`
                    <option value="${group.id}">
                        ${group.name}
                    </option>
                `);
            });
        },
        error: function(xhr, status, error) {
            console.error('Failed to fetch data:', error);
        }
    });
});
