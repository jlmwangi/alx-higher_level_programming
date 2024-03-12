#!/usr/bin/node

class Rectangle {
	constructor(w, h) {
		if (w <= 0 || h <= 0 || !h || !w)
		{
			this.width;
			this.height;
		}
		else
		{
			this.width = w;
			this.height = h;
		}
	}
	print() {
		if (this.width !== undefined && this.height !== undefined)
		{
			for (let i = 0; i < this.height; i++)
			{
				let row = '';
				for (let j = 0; j < this.width; j++)
					row += 'X';
				console.log(row);
			}
		}
		else
			console.log("undefined rectangle");
	}
	rotate() {
		let temp = this.width;
		this.width = this.height;
		this.height = temp;
	}
	double() {
		this.width *= 2;
		this.height *= 2;
	}
}

module.exports = Rectangle;
