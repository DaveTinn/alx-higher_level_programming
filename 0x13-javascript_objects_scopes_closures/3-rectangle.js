#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let idx = 0; idx < this.height; idx++) {
      let rectangle = '';
      for (let i = 0; i < this.width; i++) {
        rectangle += 'X';
      }
      console.log(rectangle);
    }
  }
}
module.exports = Rectangle;
