#!/usr/bin/node
const get = require('request');
const url = process.argv[2];

get(url, function (error, response) {
  if (error) {
    console.error('Error:', error.message);
  } else {
    console.log('code:', response.statusCode);
  }
});
