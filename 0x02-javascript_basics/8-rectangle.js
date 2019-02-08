#!/usr/bin/node
exports.Rectangle = function Rectangle (w, h) {
  if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
    return this;
  } else {
    this.width = w;
    this.height = h;
  }
};
