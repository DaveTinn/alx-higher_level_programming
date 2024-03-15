#!/usr/bin/node

const myArg = process.argv[2];
const x = parseInt(myArg);
let itr;

if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (itr = 0; itr < x; itr++) {
    console.log('C is fun');
  }
}
