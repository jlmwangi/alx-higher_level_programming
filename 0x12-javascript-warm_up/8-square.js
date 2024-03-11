#!/usr/bin/node

let args = process.argv;
let x;

if (isNaN(parseInt(args[2])))
	console.log("Missing size");
else
{
	x = parseInt(args[2]);
	for (let i = 0; i < x; i++)
	{
		let line = '';
		for (let j = 0; j < x; j++)
			line += 'X';
		console.log(line);
	}
}
