function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for (var i in uiBathrooms) {
        if (uiBathrooms[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1; // Invalid value
}

function getBedValue() {
    var uiBeds = document.getElementsByName("uiBeds");
    for (var i in uiBeds) {
        if (uiBeds[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1; // Invalid value
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");

    var sqft = document.getElementById("uiSqft").value;
    var beds = getBedValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations").value;
    var yearBuilt = document.getElementById("uiYearBuilt").value;
    var propertyType = document.getElementById("uiPropertyType").value;
    var estPrice = document.getElementById("uiEstimatedPrice");

    //var url = "http://127.0.0.1:5000/predict_home_price";
    var url = "/api/predict_home_price";

    $.post(url, {
        total_sqft: parseFloat(sqft),
        city: location,  // Ensure the key names match what your backend expects
        property_type: propertyType,
        bed: parseInt(beds),
        bath: parseInt(bathrooms),
        year_built: parseInt(yearBuilt)
    }, function(data, status) {
        console.log("Estimated price received:", data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toLocaleString() + " Dollars</h2>";
        console.log(status);
    });
}



function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }

window.onload = onPageLoad;