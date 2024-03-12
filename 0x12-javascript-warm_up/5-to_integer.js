#!/usr/bin/node

const myArg = process.argv[2];
const myInt = parseInt(myArg);

if (isNaN(myInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myInt}`);
}
