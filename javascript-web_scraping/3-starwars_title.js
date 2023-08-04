#!/usr/bin/node
/* Starrwars */
const get = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/:id';

get(url, 'utf-8', function (error, response, data) {
  if (error) {
    console.log(error);
  } else {
    const bodyObj = JSON.parse(data);
    console.log(bodyObj.title);
  }
});
