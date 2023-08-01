#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      // If w or h is equal to 0 or not a positive integer, create an empty object
      return {};
    }

    this.width = w;
    this.height = h;
  }

  toString() {
    return `Rectangle { width: ${this.width}, height: ${this.height} }`;
  }
}

module.exports = Rectangle;

  
  