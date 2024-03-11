#!/usr/bin/node

let args = process.argv;
let x = args[2];

if (isNaN(parseInt(x)))
	console.log("Missing number of occurrences");
else
{
	x = parseInt(x);
	while (x >= 1)
	{
		console.log("C is fun");
		x--;
	}
}
