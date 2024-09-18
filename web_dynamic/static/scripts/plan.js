$(document).ready(function () {
  // Retrieve the value of 'user_id' from sessionStorage
  const userId = sessionStorage.getItem("user_id");

  $.ajax({
    url: `http://127.0.0.1:5001/api/v1/users/${userId}/groups`,
    method: "GET",
    success: function (plans) {
      // Clear existing plans
      $("#plans").empty();

      // Add each plan to the plans section
      plans.forEach((plan) => {
        $("#plans").append(`
                    <div class="plan-card">
                        <h3>${plan.name}</h3>
                        <p class="amount">${plan.target_amount}</p>
                        <a href="#" class="see-plan">See plan</a>
                    </div>
                `);
      });

      
      // Add the "Create New Plan" card
      $("#plans").append(`
                <div class="plan-card">
                    <a href="${newPlanUrl}" class="new-plan">+</a>
                    <h4>Create New Plan</h4>
                </div>
            `);
    },
    error: function (xhr, status, error) {
      console.error("Failed to load plans:", status, error);
    },
  });
});
