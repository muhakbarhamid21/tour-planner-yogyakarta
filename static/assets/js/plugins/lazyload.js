// Add event listeners, interactivity, or lazy load functionality

document.addEventListener("DOMContentLoaded", function () {
  // This ensures the script runs only after the DOM is fully loaded

  // Example: Add interactivity or handle form submissions

  // Handling form submissions for TOPSIS weights input
  const form = document.querySelector("#topsisForm"); // Assuming a form with ID 'topsisForm'

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      // Extract values from the form
      const distanceWeight = document.querySelector("#distanceWeight").value;
      const priceWeight = document.querySelector("#priceWeight").value;
      const ratingWeight = document.querySelector("#ratingWeight").value;
      const facilityWeight = document.querySelector("#facilityWeight").value;

      // Validate weights and process the TOPSIS algorithm
      if (
        validateWeights(
          distanceWeight,
          priceWeight,
          ratingWeight,
          facilityWeight
        )
      ) {
        processTOPSIS(
          distanceWeight,
          priceWeight,
          ratingWeight,
          facilityWeight
        );
      } else {
        alert("Please ensure all weights add up to 100.");
      }
    });
  }
});

// Utility function to validate if weights sum up to 100
function validateWeights(distance, price, rating, facility) {
  const totalWeight =
    parseFloat(distance) +
    parseFloat(price) +
    parseFloat(rating) +
    parseFloat(facility);
  return totalWeight === 100;
}

// Example function to simulate TOPSIS processing (replace with actual implementation)
function processTOPSIS(distance, price, rating, facility) {
  // Simulate TOPSIS calculation logic or send data to a server for processing
  console.log("Processing TOPSIS with weights:", {
    distance,
    price,
    rating,
    facility,
  });
  // Update the page with the results (you can modify the DOM with the results here)
  document.querySelector("#topsisResult").innerHTML =
    "TOPSIS Result: Example Rank 1";
}
