document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.querySelectorAll(".btn-primary.btn-sm");

  editButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Mendapatkan elemen card yang terdekat dari tombol yang diklik
      const card = this.closest(".card");

      // Mengambil teks dari header h5 (Type of Attractions)
      const typeOfAttractions = card.querySelector("h5").innerText.trim(); // Mengambil teks dari h5

      // Mengambil data dari baris tabel
      const row = this.closest("tr");
      const attraction = row.children[1].innerText.trim(); // Attraction (kolom 2)
      const distance = row.children[2].innerText.trim(); // Distance (kolom 3)
      const entryPrice = row.children[3].innerText.trim(); // Entry Price (kolom 4)
      const star = row.children[4].innerText.trim(); // Star (kolom 5)
      const comment = row.children[5].innerText.trim(); // Comment (kolom 6)
      const facility = row.children[6].innerText.trim(); // Facility (kolom 7)

      // Memasukkan data ke dalam form
      document.getElementById("type-of-recreations").value = typeOfAttractions; // Mengisi Type of Attractions
      document.getElementById("attraction").value = attraction; // Mengisi Attraction
      document.getElementById("entryPrice").value = entryPrice; // Mengisi Entry Price
      document.getElementById("star").value = star; // Mengisi Star
      document.getElementById("comment").value = comment; // Mengisi Comment
      document.getElementById("facility").value = facility; // Mengisi Facility
    });
  });
});
