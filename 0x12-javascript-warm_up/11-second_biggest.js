#!/usr/bin/node
const myArgs = process.argv.slice(2);
const numOfArgs = myArgs.map(arg => parseInt(arg));

if (numOfArgs.length < 2) {
  console.log(0);
} else {
  const sortedNumOfArgs = numOfArgs.sort((a, b) => b - a);
  console.log(sortedNumOfArgs[1]);
}
