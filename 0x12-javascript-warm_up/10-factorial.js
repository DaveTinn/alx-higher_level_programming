#!/usr/bin/node
function factorial (n) {
  if (isNaN(n)) {
    return (1);
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const myInt = parseInt(process.argv[2]);
const result = factorial(myInt);
console.log(result);
