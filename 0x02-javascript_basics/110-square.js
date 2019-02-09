#!/usr/bin/node
const base = require('./109-square').Square;

function Square (size) {
  base.call(this, size, size);

  this.charPrint = (x) => {
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

module.exports = { Square };
