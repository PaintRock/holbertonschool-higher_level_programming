#!/usr/bin/node
// prints the title of a Star Wars movies
const request = require('request');
const url = process.argv[2];
const ID = '18';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;
    for (let film of data) {
      for (let character of film['characters']) {
        if (character.includes(ID)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});