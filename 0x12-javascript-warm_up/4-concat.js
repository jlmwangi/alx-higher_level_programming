#!/usr/bin/node

let args = process.argv;

if (args.length === 2)
	console.log("undefined is undefined");
else if (args.length === 3)
	console.log(args[2], "is undefined");
else if (args.length === 4)
{
	console.log(args[2], "is", args[3]);
}
