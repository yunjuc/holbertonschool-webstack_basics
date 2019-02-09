#!/usr/bin/node
const base = require('./109-square').Square;

function Square (size) {
  base.call(this, size);

  Square.prototype.charPrint = (c) => {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write(c);
        }
        console.log();
      }
    } else this.print();
  };
}

module.exports = { Square };
