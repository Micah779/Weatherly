// Lookup lat/lng for zipcode
const zipCodeInput = document.getElementById("zipCodeInput");
const zipcode = zipCodeInput.value;

const API_KEY = "AIzaSyAX2Sp73OJASXuK6wiUSbEH1KMpyrMcwC0";

// Geocode URL
const geocodeUrl = `https://maps.googleapis.com/maps/api/geocode/json?address=${zipcode}&key=${API_KEY}`

fetch(geocodeUrl)
  .then(response => response.json())
  .then(data => {
    const lat = data.results[0].geometry.location.lat
    const lng = data.results[0].geometry.location.lng

    // Init map
    const map = new google.maps.Map(document.getElementById("map"), {
      center: {lat, lng},
      zoom: 12
    })

    // Add marker at zipcode location
    new google.maps.Marker({
      position: {lat, lng},
      map: map
    })
  })