#!/usr/bin/node
const size = process.argv[2];

if (!size || isNaN(size)) {
  console.log('Missing size');
} else {
  const squareSize = parseInt(size, 10);

  for (let row = 0; row < squareSize; row++) {
    let squareRow = '';
    for (let col = 0; col < squareSize; col++) {
      squareRow += 'X';
    }
    console.log(squareRow);
  }
}
