#!/usr/bin/node
/* Write a script that prints the contents of a file */
const fs = require('fs');
const path = process.argv[2];

fs.writeFile(path, 'utf-8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
