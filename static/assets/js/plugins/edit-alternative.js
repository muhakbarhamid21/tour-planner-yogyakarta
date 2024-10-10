document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.querySelectorAll(".edit-btn");

  editButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Mengambil data dari atribut tombol
      const attractionId = this.getAttribute("data-id");
      const categoryId = this.getAttribute("data-category-id");
      const attraction = this.getAttribute("data-name");
      const lon = this.getAttribute("data-lon");
      const lat = this.getAttribute("data-lat");
      const entryPrice = this.getAttribute("data-entry_price");
      const star = this.getAttribute("data-stars");
      const comment = this.getAttribute("data-reviews");
      const facility = this.getAttribute("data-facility");

      // Memasukkan data ke dalam form
      document.getElementById("attraction-id").value = attractionId; // hidden field for ID
      document.getElementById("type-of-recreations").value = categoryId; // Mengisi Type of Attractions
      document.getElementById("attraction").value = attraction; // Mengisi Attraction
      document.getElementById("lon").value = lon; // Mengisi Long
      document.getElementById("lat").value = lat; // Mengisi Lat
      document.getElementById("entryPrice").value = entryPrice; // Mengisi Entry Price
      document.getElementById("star").value = star; // Mengisi Star
      document.getElementById("comment").value = comment; // Mengisi Comment
      document.getElementById("facility").value = facility; // Mengisi Facility
    });
  });
});
