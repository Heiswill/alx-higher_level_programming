#!/usr/bin/node
const S = require('./5-square');

class Square extends S {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let row = 0; row < this.height; row++) {
      let prints = '';
      for (let col = 0; col < this.width; col++) {
        prints += c;
      }
      console.log(prints);
    }
  }
}
module.exports = Square;
