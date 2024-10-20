document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.querySelectorAll(".edit-btn");
  const form = document.getElementById("addeditForm");

  // Fungsi untuk menangani pengisian data saat mengklik tombol edit
  editButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const attractionId = this.getAttribute("data-id");
      const categoryId = this.getAttribute("data-category-id");
      const attraction = this.getAttribute("data-name");
      const lon = this.getAttribute("data-lon");
      const lat = this.getAttribute("data-lat");
      const entryPrice = this.getAttribute("data-entry_price");
      const star = this.getAttribute("data-stars");
      const comment = this.getAttribute("data-reviews");
      const facility = this.getAttribute("data-facility");

      // Mengisi data ke dalam form
      document.getElementById("attraction-id").value = attractionId;
      document.getElementById("type-of-recreations").value = categoryId;
      document.getElementById("attraction").value = attraction;
      document.getElementById("lon").value = lon;
      document.getElementById("lat").value = lat;
      document.getElementById("entryPrice").value = entryPrice;
      document.getElementById("star").value = star;
      document.getElementById("comment").value = comment;
      document.getElementById("facility").value = facility;
    });
  });

  // Fungsi validasi form sebelum submit
  form.addEventListener("submit", function (e) {
    const category = document.getElementById("type-of-recreations").value;
    const attraction = document.getElementById("attraction").value;
    const lon = document.getElementById("lon").value;
    const lat = document.getElementById("lat").value;
    const entryPrice = document.getElementById("entryPrice").value;
    const star = document.getElementById("star").value;
    const comment = document.getElementById("comment").value;
    const facility = document.getElementById("facility").value;

    if (
      !category ||
      !attraction ||
      !lon ||
      !lat ||
      !entryPrice ||
      !star ||
      !comment ||
      !facility
    ) {
      e.preventDefault();
      alert("Please fill in all required fields.");
    } else {
      alert("Attraction successfully saved!");
    }
  });
});
