// Initialize Google Maps and the Autocomplete API
function initMap() {
    // Autocomplete for Pickup Location
    var pickupInput = document.getElementById('pickup-location');
    var pickupAutocomplete = new google.maps.places.Autocomplete(pickupInput);
    
    pickupAutocomplete.addListener('place_changed', function () {
        var place = pickupAutocomplete.getPlace();
        if (!place.geometry) {
            alert("No details available for input: '" + place.name + "'");
            return;
        }

        // Set latitude and longitude for pickup location
        document.getElementById('pickup_lat').value = place.geometry.location.lat();
        document.getElementById('pickup_lng').value = place.geometry.location.lng();
    });

    // Autocomplete for Drop Location
    var dropoffInput = document.getElementById('drop-location');
    var dropoffAutocomplete = new google.maps.places.Autocomplete(dropoffInput);
    
    dropoffAutocomplete.addListener('place_changed', function () {
        var place = dropoffAutocomplete.getPlace();
        if (!place.geometry) {
            alert("No details available for input: '" + place.name + "'");
            return;
        }

        // Set latitude and longitude for dropoff location
        document.getElementById('dropoff_lat').value = place.geometry.location.lat();
        document.getElementById('dropoff_lng').value = place.geometry.location.lng();
    });

    // Geolocation for live location functionality
    document.getElementById('set-current-location').addEventListener('click', function () {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function (position) {
                var lat = position.coords.latitude;
                var lng = position.coords.longitude;

                // Set the values in the hidden fields and display the location in the input
                document.getElementById('pickup_lat').value = lat;
                document.getElementById('pickup_lng').value = lng;

                // Reverse Geocode to get human-readable address for the current location
                var geocoder = new google.maps.Geocoder();
                var latlng = { lat: lat, lng: lng };
                geocoder.geocode({ location: latlng }, function (results, status) {
                    if (status === 'OK') {
                        if (results[0]) {
                            pickupInput.value = results[0].formatted_address;
                        } else {
                            alert('No results found');
                        }
                    } else {
                        alert('Geocoder failed due to: ' + status);
                    }
                });
            });
        } else {
            alert("Geolocation is not supported by this browser.");
        }
    });
}

// Load the Google Maps script
document.addEventListener('DOMContentLoaded', function () {
    var script = document.createElement('script');
    script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyA4gW9aZbQs35YXOCdPYOPweb6-o3JENuc&libraries=places&callback=initMap", asyncdefer;
    script.async = true;
    script.defer = true;
    document.head.appendChild(script);
});
