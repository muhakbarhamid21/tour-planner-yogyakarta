document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.querySelectorAll(".btn-primary.btn-sm");

  editButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Mendapatkan elemen card yang terdekat dari tombol yang diklik
      const card = this.closest(".card");

      // Mengambil teks dari header h5 yang ada di dalam card
      const header = card.querySelector("h5").innerText.trim();

      // Mengambil data dari baris tabel yang sesuai
      const row = this.closest("tr");
      const lowerBound = row.children[1].innerText.trim(); // Lower Bound dari kolom ke-2
      const upperBound = row.children[2].innerText.trim(); // Upper Bound dari kolom ke-3
      const weight = row.children[3].innerText.trim(); // Weight dari kolom ke-4

      // Jika header adalah Rating, cek sub-parameter Star atau Comment
      if (header === "Rating") {
        const subParameter = card.querySelector("h6").innerText.trim(); // Mengambil teks sub-parameter dari h6

        if (subParameter === "Star") {
          // Memasukkan data untuk sub-parameter Star
          document.getElementById("lowerBound").value = lowerBound; // Mengisi Lower Bound
          document.getElementById("upperBound").value = upperBound; // Mengisi Upper Bound
          document.getElementById("type-of-recreations").value = weight; // Mengisi Weight
        } else if (subParameter === "Comment") {
          // Memasukkan data untuk sub-parameter Comment
          document.getElementById("lowerBound").value = lowerBound; // Mengisi Lower Bound
          document.getElementById("upperBound").value = upperBound; // Mengisi Upper Bound
          document.getElementById("type-of-recreations").value = weight; // Mengisi Weight
        }
      } else {
        // Memasukkan data ke dalam field form sesuai dengan header lainnya
        document.getElementById("lowerBound").value = lowerBound; // Mengisi Lower Bound
        document.getElementById("upperBound").value = upperBound; // Mengisi Upper Bound
        document.getElementById("type-of-recreations").value = weight; // Mengisi Weight
      }
    });
  });
});
