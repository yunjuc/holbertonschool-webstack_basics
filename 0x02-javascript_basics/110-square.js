#!/usr/bin/node
const Rectangle = require('./9-rectangle').Rectangle;

function Square (size) {
  Rectangle.call(this, size, size);

  Square.prototype.double = () => {
    this.width *= 2;
    this.height *= 2;
  };

  Square.prototype.charPrint = (x) => {
    if (x) {
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('C');
        }
        console.log();
      }
    } else this.print();
  };
}

Square.prototype = Object.create(Rectangle.prototype);
Square.prototype.constructor = Square;

module.exports = { Square };
