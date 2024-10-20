document.addEventListener("DOMContentLoaded", () => {
  saveLocation();
});

function getAddressFromCoordinates(latitude, longitude) {
  const url = `https://nominatim.openstreetmap.org/reverse?lat=${latitude}&lon=${longitude}&format=json`;

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      const address = data.display_name;
      document.getElementById("address").innerText = `Address: ${address}`;
    })
    .catch((error) => {
      console.error("Error:", error);
      document.getElementById("address").innerText =
        "Unable to retrieve address.";
    });
}

function saveLocation() {
  // Memeriksa apakah browser mendukung Geolocation API
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        // Mendapatkan latitude dan longitude
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        // Atur cookies untuk latitude dan longitude
        document.cookie = `latitude=${latitude}; path=/; max-age=86400`; // berlaku 1 hari
        document.cookie = `longitude=${longitude}; path=/; max-age=86400`;

        console.log("Location updated in cookies:", { latitude, longitude });

        getAddressFromCoordinates(latitude, longitude);

        // // Membuat objek lokasi
        // const locationData = {
        //   latitude: latitude,
        //   longitude: longitude,
        // };

        // // Menyimpan data lokasi di sessionStorage
        // sessionStorage.setItem("currentLocation", JSON.stringify(locationData));

        // // Menampilkan pesan berhasil
        // alert("Location saved successfully in session storage!");
        // console.log("Location saved in session storage:", locationData);
      },
      (error) => {
        // Menangani kesalahan
        console.error(`Error Code: ${error.code}, Message: ${error.message}`);
        alert("Unable to retrieve location. Please allow access to location.");
      }
    );
  } else {
    alert("Geolocation is not supported by this browser.");
  }
}
