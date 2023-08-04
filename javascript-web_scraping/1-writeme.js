#!/usr/bin/node
/* Write a script that writes the contents of a file */
const fs = require('fs');
// Import 'fs' (fileStorage)
const path = process.argv[2];
// First argument is the filePath
const string1 = process.argv[3];
// Second argument is the string to write

fs.writeFile(path, string1, 'utf-8', function (error) {
  /*  Instruction to write the file following the
  path from the first arg, in utf-8, and the function is error */
  if (error) {
    console.log(error);
    // if there is an error print to console
  }
});
