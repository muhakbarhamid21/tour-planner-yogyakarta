// Add event listener to the button
document.getElementById("weightButton").addEventListener("click", function () {
  // Get values of all inputs
  const distance = parseFloat(document.getElementById("distance").value) || 0;
  const entryPrice =
    parseFloat(document.getElementById("entryPrice").value) || 0;
  const rating = parseFloat(document.getElementById("rating").value) || 0;
  const facility = parseFloat(document.getElementById("facility").value) || 0;

  // Get values of sub-inputs for C3.1 and C3.2
  const star = parseFloat(document.getElementById("star").value) || 0;
  const comment = parseFloat(document.getElementById("comment").value) || 0;

  // Calculate the total of C1, C2, C3, and C4
  const total = distance + entryPrice + rating + facility;

  // Calculate the total of C3.1 (Star) and C3.2 (Comment)
  const totalC3Sub = star + comment;

  // Initialize an empty error message
  let errorMessage = "ERROR!!!\n- Your input is wrong.\n";

  // Check if total of C1, C2, C3, and C4 is equal to 100
  if (total !== 100) {
    // Add error message for total of C1, C2, C3, and C4
    errorMessage +=
      "- Total weighting for C1, C2, C3, and C4 must be exactly 100. Your total is " +
      total +
      ".\n";
  }

  // Check if total of C3.1 (Star) and C3.2 (Comment) is equal to 100
  if (totalC3Sub !== 100) {
    // Add error message for total of C3.1 and C3.2
    errorMessage +=
      "- Total weighting for C3.1 and C3.2  must be exactly 100. Your total for C3 is " +
      totalC3Sub +
      ".\n";
  }

  // If there is any error, show the alert
  if (total !== 100 || totalC3Sub !== 100) {
    alert(errorMessage);
  } else {
    // Show success message if all totals are correct
    //alert("Success: All weightings are correct! You can proceed.");
    //LANJUT
  }
});
