// Initialize and add the map for the contact page, documentation from the Google Maps API
   function initMap() {
     // The location of Caffeine, CA (fictional)
     const caffeine = { lat: 37.7694, lng: -122.4862 };
     // The map, centered at California 
     const map = new google.maps.Map(document.getElementById("map"), {
       zoom: 10,
       center: caffeine,
     });
     // The marker, positioned at Caffeine, CA
     const marker = new google.maps.Marker({
       position: caffeine,
       map: map,
     });
   }