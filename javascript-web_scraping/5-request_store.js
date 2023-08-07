#!/usr/bin/node
const url = process.argv[2];
const path = process.argv[2];
const request = require('request');
const fs = require('fs');

request(url, functon (error, response, body)) {
  if(error) {
    console.log(error);
  }else{
    fs.writeFile(path, 'utf-8', function(err)) {
      if (err) {
        console.log(err);
    }
  }
}
}