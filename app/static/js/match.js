function initMap() {
	console.log('aaaa')
	var mapOptions = {
		zoom: 8,
		center: new google.maps.LatLng(37.5, -122),
		mapTypeId: 'roadmap'
	};
	var map = new google.maps.Map(document.getElementById('map'), mapOptions);

	var goldenGatePosition = { lat: 37.8199, lng: -122.4783 };
	var marker = new google.maps.Marker({
		position: goldenGatePosition,
		map: map,
		title: 'Golden Gate Bridge'
	});

}