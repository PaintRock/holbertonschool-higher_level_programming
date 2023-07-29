#!/usr/bin/node

#!/usr/bin/node

/* eslint quotes: ["error", "single"], semi: ["error", "always"] */

function add(a, b) {
  return a + b;
}

const firstInteger = parseInt(process.argv[2]);
const secondInteger = parseInt(process.argv[3]);

if (isNaN(firstInteger) || isNaN(secondInteger)) {
  console.log(NaN);
} else {
  const result = add(firstInteger, secondInteger);
  console.log(result);
}
