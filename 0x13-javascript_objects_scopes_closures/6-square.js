#!/usr/bin/node

const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        if (c) {
          row += c;
        } else {
          row += 'X';
        }
      }
      console.log(row);
    }
  }
}

module.exports = Square;
