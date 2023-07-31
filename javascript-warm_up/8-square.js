#!/usr/bin/node
const size = process.argv[2];

if (!size || isNaN(size)) {
  console.log("Missing size");
} else {
  const squareSize = parseInt(size, 10);
  let square = "";

  for (let row = 0; row < squareSize; row++) {
    for (let col = 0; col < squareSize; col++) {
      square += "X";
      if (col < squareSize - 1) {
        square += " ";
      }
    }
    square += "\n";
  }

  console.log(square);
}
