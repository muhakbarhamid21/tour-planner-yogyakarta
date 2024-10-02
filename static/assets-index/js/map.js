// Initialize the map and set its view to Yogyakarta
var map = L.map("map").setView([-7.797068, 110.370529], 13);

// Load and display OpenStreetMap tiles
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

// Marker to show search results
var searchMarker;

// Function to search location using Leaflet Geocoder
function searchLocation(query) {
  L.Control.Geocoder.nominatim().geocode(query, function (results) {
    if (results.length > 0) {
      var result = results[0];

      // If there is already a marker, remove it
      if (searchMarker) {
        map.removeLayer(searchMarker);
      }

      // Add a marker to the search result location
      searchMarker = L.marker(result.center)
        .addTo(map)
        .bindPopup(result.name)
        .openPopup();

      // Zoom to the result location
      map.setView(result.center, 13);
    } else {
      alert("Location not found.");
    }
  });
}

// Event listener for the search button
document
  .getElementById("search-btn-location")
  .addEventListener("click", function () {
    var query = document.getElementById("search-box-location").value;
    searchLocation(query);
  });
