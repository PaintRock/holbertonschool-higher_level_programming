#!/usr/bin/node
/* Write a script that writes the contents of a file */
const fs = require('fs');
const path = process.argv[2];
const text = process.argv[3];

fs.writeFile(path, text, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
