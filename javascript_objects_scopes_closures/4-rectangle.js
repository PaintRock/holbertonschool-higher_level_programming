#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

rotate () {
  const x = this.height;
  this.height = this.width;
  this.width = x;
}

double () {
  this.height *= 2;
  this.width *= 2;
}
}
module.exports = Rectangle;
