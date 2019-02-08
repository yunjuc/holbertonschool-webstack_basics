#!/usr/bin/node
const fs = require('fs');
const path = process.argv[2];
const message = process.argv[3];

fs.writeFile(path, message, function (err) {
  if (err) {
    console.log(err);
  }
});
