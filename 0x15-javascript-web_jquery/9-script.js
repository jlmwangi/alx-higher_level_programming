//fetches and displays the value of hello from the fetch
document.addEventListener('DOMContentLoaded', function() {
	$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
		//extract the greeting from the responseg
		const greeting = data.hello;
		//update divhelllo with the greeting
		$('div#hello').text(greeting);
	});
});
