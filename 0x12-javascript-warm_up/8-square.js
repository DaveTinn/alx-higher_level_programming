#!/usr/bin/node
const sizeOfSquare = process.argv[2];
const myInt = parseInt(sizeOfSquare);

if (isNaN(myInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myInt; i++) {
    let square = '';
    for (let d = 0; d < myInt; d++) {
      square += 'X';
    }
    console.log(square);
  }
}
