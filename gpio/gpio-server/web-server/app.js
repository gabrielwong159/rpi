$.ajax({
	type: 'GET',
	url: 'http://10.21.113.244:5000/neopixel',

	success: function(response) {
		console.log(response);
	},
	error: function(error) {
		console.log(error.message);
	}
});
