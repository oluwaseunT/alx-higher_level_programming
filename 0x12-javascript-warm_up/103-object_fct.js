#!/usr/bin/node
// 103-object_fct.js
// Update this script by adding a new function incr that increments the integer value

const myObject = {
	type: 'object',
	value: 12
};
console.log(myObject);

myObject.incr = function () {
	this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
