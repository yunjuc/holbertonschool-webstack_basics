#!/usr/bin/node
const Rectangle = require('./9-rectangle').Rectangle;

function Square (size) {
  Rectangle.call(this, size, size);

  Square.prototype.double = () => {
    this.width *= 2;
    this.height *= 2;
  };
}

Square.prototype = Object.create(Rectangle.prototype);
Square.prototype.constructor = Square;

module.exports = { Square };
