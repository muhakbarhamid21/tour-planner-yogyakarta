document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.querySelectorAll(".btn-primary.btn-sm");

  editButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Mengambil data dari atribut data-parameter dan data-criteria pada tombol
      const parameter = button.getAttribute("data-parameter");
      const criteria = button.getAttribute("data-criteria");
      const criteria_id = button.getAttribute("data-id");

      console.log(parameter, criteria);

      // Memasukkan data ke dalam form
      document.getElementById("parameter").value = parameter; // Mengisi Parameter
      document.getElementById("criteria").value = criteria; // Mengisi Criteria
      document.getElementById("criteria_id").value = criteria_id; // Mengisi Criteria
    });
  });

  // Menangani form submission
  const form = document.getElementById("editcriteriaFrom");
  form.addEventListener("submit", function (e) {
    e.preventDefault(); // Mencegah pengiriman form secara default

    // Lakukan pengiriman form atau tindakan lainnya
    // Setelah berhasil, tampilkan pesan alert sukses
    alert("Criteria successfully changed!");

    // Jika perlu, lanjutkan pengiriman form secara manual setelah alert
    form.submit(); // Lanjutkan pengiriman form setelah alert ditampilkan
  });
});
