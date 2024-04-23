#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
	if (error) {
		console.error(error.message);
		return;
	}

	const movies = JSON.parse(body).results;
	const charId = 18;
	let count = 0;

	movies.forEach(movie => {
		if (movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charId}/`)) {
			count++;
		}
	});
	console.log(`${count}`);
});
