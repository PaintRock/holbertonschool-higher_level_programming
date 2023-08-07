#!/usr/bin/node
const url = process.argv[2];
const path = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, 'utf-8', functon (error, response, body) {
  if (error) {
    console.log(error);
  } else {}
    fs.writeFile(path, 'utf-8', function(error) {
      if (error) {
        console.log(error);
    }
  })
});
