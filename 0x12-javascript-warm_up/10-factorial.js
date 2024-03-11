#!/usr/bin/node

function factorial(n)
{
	if (isNaN(n) || n <= 0 || n === 1)
	{
		console.log(1);
	}

	let res = n * factorial(n - 1);
	console.log(res);
}
