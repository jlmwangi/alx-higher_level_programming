//fetches data from the api
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
	//on success set characters name to div_character
	$('div#character').text(data.name);
});
