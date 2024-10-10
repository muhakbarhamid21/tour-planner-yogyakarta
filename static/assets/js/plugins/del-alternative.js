document.addEventListener("DOMContentLoaded", function () {
  const deleteButtons = document.querySelectorAll(".btn-danger");

  deleteButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const attractionId = this.getAttribute("data-id");

      if (confirm("Apakah Anda yakin ingin menghapus atraksi ini?")) {
        fetch(`/dss/alternative/delete/${attractionId}`, {
          method: "DELETE",
        })
          .then((response) => {
            if (response.ok) {
              alert("Atraksi berhasil dihapus!");
              // Refresh atau hapus baris dari tabel
              this.closest("tr").remove();
            } else {
              return response.json().then((data) => {
                alert(`Gagal menghapus atraksi. Pesan: ${data.message}`);
              });
            }
          })
          .catch((error) => {
            alert(`Terjadi kesalahan: ${error}`);
          });
      }
    });
  });
});
