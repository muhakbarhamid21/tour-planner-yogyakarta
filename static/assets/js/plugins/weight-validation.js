document.addEventListener("DOMContentLoaded", function () {
  const button = document.getElementById("weightButton");
  const distanceInput = document.getElementById("distance");
  const entryPriceInput = document.getElementById("entryPrice");
  const ratingInput = document.getElementById("rating");
  const facilityInput = document.getElementById("facility");
  const starInput = document.getElementById("star");
  const commentInput = document.getElementById("comment");

  let debounceTimer;

  function validateWeights() {
    // Get values of all inputs
    const distance = parseFloat(distanceInput.value) || 0;
    const entryPrice = parseFloat(entryPriceInput.value) || 0;
    const rating = parseFloat(ratingInput.value) || 0;
    const facility = parseFloat(facilityInput.value) || 0;
    const star = parseFloat(starInput.value) || 0;
    const comment = parseFloat(commentInput.value) || 0;

    // Calculate the total of C1, C2, C3, and C4
    const total = distance + entryPrice + rating + facility;
    // Calculate the total of C3.1 (Star) and C3.2 (Comment)
    const totalC3Sub = star + comment;

    // Check if all inputs are filled (not zero) before validating
    const allInputsFilled = [distance, entryPrice, rating, facility, star, comment].every(value => value > 0);

    // Initialize an empty error message
    let errorMessage = "ERROR!!!\n- Your input is wrong.\n";

    if (!allInputsFilled) {
      button.disabled = true; // Disable the button if not all inputs are filled
      return; // Exit the function if not all inputs are filled
    }

    // Check if total of C1, C2, C3, and C4 is equal to 100
    if (total !== 100) {
      errorMessage += `- Total weighting for C1, C2, C3, and C4 must be exactly 100. Your total is ${total}.\n`;
    }

    // Check if total of C3.1 (Star) and C3.2 (Comment) is equal to 100
    if (totalC3Sub !== 100) {
      errorMessage += `- Total weighting for C3.1 and C3.2 must be exactly 100. Your total for C3 is ${totalC3Sub}.\n`;
    }

    // If totals are incorrect, disable the button and show an alert
    if (total !== 100 || totalC3Sub !== 100) {
      button.disabled = true; // Disable the button
      alert(errorMessage);
    } else {
      button.disabled = false; // Enable the button
    }
  }

  function debounceValidateWeights() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(validateWeights, 500); // Delay of 500ms
  }

  // Attach event listeners to all inputs to re-check totals on input change
  [distanceInput, entryPriceInput, ratingInput, facilityInput, starInput, commentInput].forEach(input => {
    input.addEventListener("input", debounceValidateWeights);
  });

  // Initial check when the page is loaded
  validateWeights();
});
