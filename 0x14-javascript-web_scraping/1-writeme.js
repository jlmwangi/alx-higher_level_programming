#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
let fileWrite = process.argv[3];

fs.writeFile(filePath, fileWrite, 'utf-8', (err) => {
	if (err) {
		console.error(err);
		return;
	}
});
