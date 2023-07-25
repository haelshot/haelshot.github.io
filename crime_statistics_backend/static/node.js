var map = L.map('map').setView([0, 0], 2);

var marker = L.marker([51.5, -0.09]).addTo(map);

var googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
    minZoom: 2,
    maxZoom: 18,
    noWrap: true,
    subdomains:['mt0','mt1','mt2','mt3']
});

googleStreets.addTo(map);

var polygon = L.polygon([
    [51.509, -0.08],
    [51.503, -0.06],
    [51.51, -0.047]
]).addTo(map);

var circle = L.circle([51.508, -0.11], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
}).addTo(map);


map.on('click', function (e) {
  var lat = e.latlng.lat;
  var lng = e.latlng.lng;

  // Use Leaflet AJAX plugin to perform reverse geocoding
  var url = 'https://nominatim.openstreetmap.org/reverse?format=json&lat=' + lat + '&lon=' + lng;
  fetch(url)
      .then(response => response.json())
      .then(data => {
          var country = data.address.country;
          console.log('Clicked Country:', country);

          // Set the country name in the hidden form field
          document.getElementById('countryNameField').value = country;

          // Submit the form to the Django server
          document.getElementById('countryForm').submit();
      });
});
document.getElementById('countrySelect').addEventListener('change', function() {
    const selectedOption = this.value;

    if (selectedOption) {
        openPopup(selectedOption);
    }
});

function openPopup() {
    const popupWidth = 400;
    const popupHeight = 300;
    const leftPosition = (screen.width - popupWidth) / 2;
    const topPosition = (screen.height - popupHeight) / 2;

    const popupUrl = "{% url 'report' %}"; // Replace this with the URL of the popup content

    window.open(popupUrl, 'Popup', `width=${popupWidth}, height=${popupHeight}, top=${topPosition}, left=${leftPosition}, resizable=yes, scrollbars=yes`);
}

