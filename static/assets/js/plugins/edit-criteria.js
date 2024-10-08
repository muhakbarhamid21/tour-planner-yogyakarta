document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.querySelectorAll(".btn-primary.btn-sm");

  editButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Mendapatkan elemen row (baris tabel) terdekat dari tombol yang diklik
      const row = this.closest("tr");

      // Mengambil data dari baris tabel
      const parameter = row.children[1].innerText.trim(); // Parameter (kolom ke-2)
      const criteria = row.children[2].innerText.trim(); // Criteria (kolom ke-3)

      // Memasukkan data ke dalam form
      document.getElementById("parameter").value = parameter; // Mengisi Parameter
      document.getElementById("criteria").value = criteria; // Mengisi Criteria
    });
  });
});
