#!/usr/bin/node
// Check the number of arguments
const numOfArgs = process.argv.length - 2;
// Print the message depending on the number of arguments
if (numOfArgs === 0) {
  console.log('No argument');
} else if (numOfArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
