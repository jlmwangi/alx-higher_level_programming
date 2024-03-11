#!/usr/bin/node

let args = process.argv;
let firstArg = args[2];

if (firstArg === undefined)
	console.log("No argument");
else
	console.log(firstArg);
