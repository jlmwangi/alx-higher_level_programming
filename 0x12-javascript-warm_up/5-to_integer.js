#!/usr/bin/node

let args = process.argv;

if (isNaN(parseInt(args[2])))
	console.log("Not a number");
else
	console.log("My number:", args[2]);
