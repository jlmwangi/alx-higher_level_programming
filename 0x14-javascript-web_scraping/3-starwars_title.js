#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const episode = parseInt(movieId, 10);

request(`https://swapi-api.alx-tools.com/api/films/${episode}`, (error, response, body) => {
	if (error) {
		console.error(error.message);
		return;
	}
	const movie = JSON.parse(body);
	console.log(movie.title);
});
