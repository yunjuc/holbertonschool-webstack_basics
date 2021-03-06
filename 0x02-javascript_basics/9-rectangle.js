#!/usr/bin/node
exports.Rectangle = function Rectangle (w, h) {
  if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
    return this;
  } else {
    this.width = w;
    this.height = h;
  }

  this.print = () => {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  };
};
