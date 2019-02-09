#!/usr/bin/node
const Rectangle = require('./9-rectangle').Rectangle;

function Square (size) {
  Rectangle.call(this, size, size);

  this.double = () => {
    this.width *= 2;
    this.height *= 2;
  };
}

module.exports = { Square };
