#!/usr/bin/node

const args = process.argv.slice(2).map(num => parseInt(num));
const sorted = args.sort((a, b) => a < b);

if (sorted.length <= 1)
	console.log(0);
else
	console.log(sorted[1]);
