#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];

fs.readFile(path, 'utf-8', function (err, data) {
  if (err) return console.log(err);
  process.stdout.write(data);
});
