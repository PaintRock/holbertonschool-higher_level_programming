#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

// Update the value of 'value' property
const updatedObject = { ...myObject, value: 89 };

console.log(updatedObject);
