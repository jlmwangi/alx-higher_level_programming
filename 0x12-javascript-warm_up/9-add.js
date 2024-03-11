#!/usr/bin/node

function add(a, b)
{
	if (isNaN(a) || isNaN(b))
	{
		console.log("NaN");
	}
	else
	{
		console.log(a + b);
	}
}

let arg1 = parseInt(process.argv[2]);
let arg2 = parseInt(process.argv[3]);

add(arg1, arg2);
