#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
	charPrint(c) {
		if (c === undefined)
			super.print();
		else
		{
			if (this.width !== undefined && this.height !== undefined)
			{
				for (let i = 0; i < this.height; i++)
				{
					let row = '';
					for (let j = 0; j < this.width; j++)
					{
						row += c;
					}
					console.log(row);
				}
			}
			else
			{
				console.log("undefined");
			}
		}
}
}

module.exports = Square;
