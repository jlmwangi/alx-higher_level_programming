//fetches and lists title for all movies
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
	//loop through each film in the results array
	data.results.forEach(function(film) {
		//create a new list for each film title
		const listItem = $('<li>').text(film.title);
		//append each list item in the html tag ul#list_movies
		$('ul#list_movies').append(listItem);
	});
});
