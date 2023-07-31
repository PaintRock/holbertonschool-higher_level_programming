#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  // Convert arguments to an array of integers
  const numbers = args.map(Number);

  // Sort the array in ascending order
  const sortedNumbers = numbers.sort((a, b) => a - b);

  // Get the second last element in the sorted array
  const secondBiggest = sortedNumbers[sortedNumbers.length - 2];

  console.log(secondBiggest);
}
