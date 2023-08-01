#!/usr/bin/node

// main.js

// Assuming you have '100-data.js' in the same directory with the following content:
// module.exports = [1, 2, 3, 4, 5];

const list = require('./100-data.js');

const newArray = list.map((value, index) => value * index);

console.log('Initial List:');
console.log(list);

console.log('\nNew List:');
console.log(newArray);
