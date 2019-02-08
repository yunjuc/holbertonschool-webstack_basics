#!/usr/bin/node
const list = require('./100-data').list;
const res = list.map((x, idx) => {
  return x * idx;
});

console.log(list);
console.log(res);
