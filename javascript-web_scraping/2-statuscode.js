#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error('Error:', error.message);
  } else {
    console.log('code:', response.statusCode);
  }
});
