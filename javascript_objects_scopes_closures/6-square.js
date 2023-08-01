#!/usr/bin/node

const Square = require ('./5-sauare');

class Square extends Square {
  constructor (size) {
    super(size,size);
  }

charPrint (c) {
  if (c === 'undefined) {
      c = 'X')
    }
    if (this.size && this.size) {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    }
module.exports = Square; 