#!/usr/bin/node
const dict = require('./101-data').dict;

const val = new Set(Object.keys(dict).map(x => dict[x]));

let newDict = {};

for (const x of val) {
  let id = [];
  for (const y in dict) {
    if (x === dict[y]) {
      id.push(y);
    }
    newDict[x] = id;
  }
}

console.log(newDict);
