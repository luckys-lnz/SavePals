$(document).ready(function () {
  function loadTransactions() {
    const userFilter = $("select:first").val(); // Get selected user filter
    const planFilter = $("select:last").val(); // Get selected plan filter

    let apiUrl = "";
    // Retrieve the value of 'user_id' from sessionStorage
    const userId = sessionStorage.getItem("user_id");

    // Determine API URL based on filters
    if (userFilter && planFilter) {
      // If both filters are true, construct a URL that handles both
      apiUrl = `http://127.0.0.1:5001/api/v1/users/${userId}/groups/${planFilter}/transactions`;
    } else if (planFilter) {
      apiUrl = `http://127.0.0.1:5001/api/v1/groups/${planFilter}/transactions`;
    } else {
      apiUrl = `http://127.0.0.1:5001/api/v1/users/${userId}/transactions`;
    }

    $.ajax({
      url: apiUrl,
      method: "GET",
      data: {
        user: userFilter,
        plan: planFilter,
      },
      success: function (transactions) {
        console.log("Transactions:", transactions);

        // Destructure contributions and payments from the transactions object
        const { contributions = [], payments = [] } = transactions;

        // Clear existing transactions in the list
        $("#list-transactions").empty();

        // Handle contributions
        contributions.forEach((contribution) => {
          const user = contribution.user || {}; // Provide empty object fallback
          const group = contribution.group || {}; // Provide empty object fallback
          const firstName = user.first_name || "Unknown";
          const groupName = group.name || "No Group";

          // Append the contribution details to the list
          $("#list-transactions").append(`
            <li>
              <span>${firstName}</span>
              <span>${contribution.amount}</span>
              <span>${groupName}</span>
            </li>
          `);
        });

        // Handle payments
        payments.forEach((payment) => {
          const user = payment.user || {}; // Provide empty object fallback
          const group = payment.group || {}; // Provide empty object fallback
          const firstName = user.first_name || "Unknown";
          const groupName = group.name || "No Group";

          // Append the payment details to the list
          $("#list-transactions").append(`
            <li>
              <span>${firstName}</span>
              <span>${payment.amount}</span>
              <span>${groupName}</span>
            </li>
          `);
        });
      },
      error: function (xhr, status, error) {
        console.error("Failed to load transactions:", status, error);
      },
    });
  }

  // Load transactions on page load
  loadTransactions();

  // Reload transactions when filters change
  $(".filter select").on("change", function () {
    loadTransactions();
  });
});

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
