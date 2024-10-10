document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.querySelectorAll(".btn-primary.btn-sm");

  editButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Mendapatkan elemen row (baris tabel) terdekat dari tombol yang diklik
      const row = this.closest("tr");

      // Mengambil data dari baris tabel
      const fullname = row.children[1].innerText.trim(); // Fullname (kolom ke-2)
      const username = row.children[2].innerText.trim(); // Username (kolom ke-3)
      const email = row.children[3].innerText.trim(); // Email (kolom ke-4)

      // Memasukkan data ke dalam form
      document.getElementById("fullname").value = fullname; // Mengisi Fullname
      document.getElementById("username").value = username; // Mengisi Username
      document.getElementById("email").value = email; // Mengisi Email

      // Kosongkan password karena kita tidak ingin menampilkan hash password
      document.getElementById("password").value = ""; // Mengosongkan password untuk alasan keamanan
    });
  });
});
