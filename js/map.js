//Data
function myEvents(arr)
{
    var xmlhttp = new XMLHttpRequest();
    var url = "photo/json";

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            var myArr = JSON.parse(xmlhttp.responseText);

            return myArr
        }
    }
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}


//Angular App Module and Controller
var MapModule = angular.module('mapsApp', [])
.controller('EventBoxCtrl', function ($scope) {
	$scope.events = [
    {
        event : 'Toronto',
        desc : 'This is the best event in the world!',
        lat : 43.7000,
        long : -79.4000
    },
    {
        event : 'New York',
        desc : 'This event is aiiiiite!',
        lat : 40.6700,
        long : -73.9400
    },
    {
        event : 'Chicago',
        desc : 'This is the second best event in the world!',
        lat : 41.8819,
        long : -87.6278
    },
    {
        event : 'Los Angeles',
        desc : 'This event is live!',
        lat : 34.0500,
        long : -118.2500
    },
    {
        event : 'Las Vegas',
        desc : 'Sin event...\'nuff said!',
        lat : 36.0800,
        long : -115.1522
    }
];

var map = {};
var redDot = new google.maps.MarkerImage(
    "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|C92A2A",
    null, /* size is determined at runtime */
    null, /* origin is 0,0 */
    null, /* anchor is bottom center of the scaled image */
    new google.maps.Size(20, 34)
);
var blueDot = new google.maps.MarkerImage(
    "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|2F4AC9",
    null, /* size is determined at runtime */
    null, /* origin is 0,0 */
    null, /* anchor is bottom center of the scaled image */
    new google.maps.Size(20, 34)
); 


var mapOptions = {
    zoom: 4,
    center: new google.maps.LatLng(40.0000, -98.0000),
    // mapTypeId: google.maps.MapTypeId.TERRAIN
	
}

$scope.map = new google.maps.Map(document.getElementById('map'), mapOptions);

$scope.markers = [];

var infoWindow = new google.maps.InfoWindow();

var createMarker = function (info){

    // var image='img/red_marker.png'
    var marker = new google.maps.Marker({
        map: $scope.map,
        position: new google.maps.LatLng(info.lat, info.long),
        title: info.event,
		icon: redDot
    });
    marker.content = '<div class="infoWindowContent">' + info.desc + '</div>';
    
    google.maps.event.addListener(marker, 'click', function(){
        infoWindow.setContent('<h2>' + marker.title + '</h2>' + marker.content);
        infoWindow.open($scope.map, marker);
    });
    $scope.markers.push(marker);
    return marker;
    
}  

for (i = 0; i < $scope.events.length; i++){
    map[i] = createMarker($scope.events[i]);
	$scope.events[i].map_id = i;
}

$scope.openInfoWindow = function(e, selectedMarker){
    e.preventDefault();
    google.maps.event.trigger(selectedMarker, 'click');
}

    $scope.hoverIn = function(map_id) {
        map[map_id].setIcon(blueDot);
    }

    $scope.hoverOut = function(map_id) {
        map[map_id].setIcon(redDot);
    }

});