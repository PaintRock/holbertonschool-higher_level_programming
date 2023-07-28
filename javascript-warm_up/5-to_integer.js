#!/usr/bin/node

const args = process.argv.slice(2);
const number = parseInt(args[0], 10);

if (!isNaN(number)) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
