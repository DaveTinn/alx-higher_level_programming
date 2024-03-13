#!/usr/bin/node
class Square extends require('./5-square.js') {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let idx = 0; idx < this.height; idx++) {
        let square = '';
        for (let i = 0; i < this.width; i++) {
          square += c;
        }
        console.log(square);
      }
    }
  }
}
module.exports = Square;
