$(document).ready(function () {
  function loadTransactions() {
    const planFilter = $("select:first").val(); // Get selected user filter
    const userFilter = $("select:last").val(); // Get selected plan filter

    let apiUrl = "";
    // Retrieve the value of 'user_id' from sessionStorage
    const userId = sessionStorage.getItem("user_id");
    

    // Determine API URL based on filters
    if (userFilter && planFilter) {
      // If both filters are true, construct a URL that handles both
      apiUrl = `http://127.0.0.1:5001/api/v1/users/${userId}/groups/${planFilter}/transactions`;
    } else {
      apiUrl = `http://127.0.0.1:5001/api/v1/groups/${planFilter}/transactions`;
    }

    $.ajax({
      url: apiUrl,
      method: "GET",
      data: {
        user: userFilter,
        plan: planFilter,
      },
      success: function (transactions) {
        // Destructure contributions and payments from the transactions object
        const { contributions = [], payments = [] } = transactions;

        // Handle empty transactions
        if (contributions.length == 0 && payments.length == 0) {
          // Display a message if no transaction is found
          $("#list-transactions")
            .empty()
            .append("<p>No transactions found.</p>");
          return;
        }

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

  // Function to load groups (plans) based on userId
  function loadGroups() {
    $.ajax({
      url: `http://127.0.0.1:5001/api/v1/users/${userId}/groups`,
      method: "GET",
      dataType: "json",
      success: function (groups) {
        const $select = $("#plan-select");
        $select.empty(); // Clear any existing options
        $select.append('<option value="">Select Plan</option>'); // Default option

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
        console.error("Failed to fetch groups:", error);
      },
    });
  }

  // Function to load and display group details based on selected plan
  function displayGroupDetails(groupId) {
    $.ajax({
      url: `http://127.0.0.1:5001/api/v1/groups/${groupId}`,
      method: "GET",
      dataType: "json",
      success: function (group) {
        if (!group || !group.name) {
          // Display a message if no group is found
          $("#group-card").empty().append("<p>No plan found.</p>");
          $("#contribution-card").empty();
          $("#withdrawal-card").empty();
          return;
        }

        // Clear existing content
        $("#group-card").empty();
        $("#contribution-card").empty();
        $("#withdrawal-card").empty();

        // Append the group details to the group card
        $("#group-card").append(`
          <h4>${group.name}</h4>
          <div class="group-goal">
            <div>
              <p>Group Balance</p>
              <h5>$40,000</h5>
            </div>
            <div>
              <p>Target</p>
              <h5>$${group.target_amount}</h5>
            </div>
            <div>
              <p>Members</p>
              <h5>${group.number_members}</h5>
            </div>
            <h5>Group Progress</h5>
            <div class="progress-container">
              <div class="progress-bar" style="width: ${group.progress}%"></div>
            </div>
          </div>
        `);

        // Append the contribution card details
        $("#contribution-card").append(`
          <h4>My Contribution</h4>
          <div class="group-goal">
            <div>
              <h3 class="amount">$1000</h3>
            </div>
            <div>
              <a href="${contributeURL}" class="create-button">+</a>
              <h5>Contribute</h5>
            </div>
          </div>
          <h5>My Progress</h5>
          <div class="progress-container">
            <div class="progress-bar" style="width: ${group.contribution_progress}%"></div>
          </div>
        `);

        // Append the withdrawal card details
        $("#withdrawal-card").append(`
          <h4>Wallet</h4>
          <h2 class="amount">$10,000</h2>
          <h5>Amount Available for Withdrawal</h5>
          <button class="withdraw-btn">Withdraw</button>
        `);
      },
      error: function (xhr, status, error) {
        console.error("Failed to load group details:", status, error);
      },
    });
  }

  // Event listener for when the plan selection changes
  $("#plan-select").change(function () {
    const selectedGroupId = $(this).val();
    if (selectedGroupId) {
      displayGroupDetails(selectedGroupId); // Load and display group details for the selected plan
    } else {
      // Clear cards if no plan is selected
      $("#group-card").empty();
      $("#contribution-card").empty();
      $("#withdrawal-card").empty();
    }
  });

  // Initial load of groups when the document is ready
  loadGroups();
});
