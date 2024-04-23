#!/usr/bin/node

const request = require('request');

const urlrequest = process.argv[2];


request(urlrequest, (error, response, body) => {
	if (error) {
		console.error(error);
		return;
	}

	const tasks = JSON.parse(body);
	const completedTasks = {}

	tasks.forEach(task => {
		if (task.completed) {
			if (completedTasks[task.userId]) {
				completedTasks[task.userId]++;
			}
			else {
				completedTasks[task.userId] = 1;
			}
		}
	});
	for (const userId in completedTasks) {
		console.log(`${userId}: ${completedTasks[userId]}`);
	}
});
