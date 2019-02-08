#!/usr/bin/node
const fs = require('fs');
const a = process.argv[2];
const b = process.argv[3];
const path = process.argv[4];

fs.readFile(a, 'utf-8', (err, data) => {
  if (err) throw err;
  fs.writeFile(path, data);
});

fs.readFile(b, 'utf-8', (err, data) => {
  if (err) throw err;
  fs.appendFile(path, data);
});
