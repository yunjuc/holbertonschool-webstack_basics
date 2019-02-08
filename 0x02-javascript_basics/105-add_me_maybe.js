#!/usr/bin/node
exports.addMeMaybe = function (x, func) {
  x += 1;
  func(x);
};
