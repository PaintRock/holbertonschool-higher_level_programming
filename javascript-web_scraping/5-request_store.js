#!/usr/bin/node
const url = process.argv[2];
const path = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, 'utf-8', function (error, response, path) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(file, path, 'utf-8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});