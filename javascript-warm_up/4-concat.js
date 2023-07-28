#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0] && args[1]) {
  console.log(args[0] + args[1]);
} else {
  console.log('No argument');
}

