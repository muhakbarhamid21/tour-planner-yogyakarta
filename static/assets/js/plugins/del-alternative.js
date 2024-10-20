document.addEventListener("DOMContentLoaded", function () {
  const deleteButtons = document.querySelectorAll(".btn-danger");

  deleteButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const attractionId = this.getAttribute("data-id");

      if (confirm("Are you sure you want to delete this attraction?")) {
        fetch(`/dss/alternative/delete/${attractionId}`, {
          method: "DELETE",
        })
          .then((response) => {
            if (response.ok) {
              alert("Attraction successfully deleted!");
              // Refresh atau hapus baris dari tabel
              this.closest("tr").remove();
            } else {
              return response.json().then((data) => {
                alert(`Failed to delete attraction. Message: ${data.message}`);
              });
            }
          })
          .catch((error) => {
            alert(`There is an error: ${error}`);
          });
      }
    });
  });
});
