function initMap() {

	function initialize() {
		let locInitInput = document.getElementsByName('loc')[0].value.split(',');
		var locInit = { lat: parseFloat(locInitInput[0]), lng: parseFloat(locInitInput[1]) };
		var map = new google.maps.Map(document.getElementById('map'), {
			zoom: 15,
			center: locInit
		});
		document.getElementsByName('loc').forEach((l, i) => {
			let locInput = l.value.split(',');
			var loc = { lat: parseFloat(locInput[0]), lng: parseFloat(locInput[1]) };
			addMarker(loc, map, document.getElementsByName('id')[i].value);

		});
	}

	function addMarker(location, map, id) {
		var image = {
			url: '../static/images/float-chave.svg',
			size: new google.maps.Size(72, 59),
			origin: new google.maps.Point(0, 0),
			labelOrigin: new google.maps.Point(-10, 0),
			anchor: new google.maps.Point(0, 32)
		};
		var marker = new google.maps.Marker({
			position: location,
			label: `${Math.floor(Math.random() * 51) + 50}%`,
			map: map,
			animation: google.maps.Animation.DROP,
			icon: image,
			id: id,
		});
		google.maps.event.addListener(marker, 'click', function () {
			window.location.href = `/property/${marker.id}`;
		});
	}

	google.maps.event.addDomListener(window, 'load', initialize);
}