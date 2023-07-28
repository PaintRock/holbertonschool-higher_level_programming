#!/usr/bin/node

/* eslint quotes: ["error", "single"], semi: ["error", "always"] */

const args = process.argv.slice(2);
const x = parseInt(args[0]);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
