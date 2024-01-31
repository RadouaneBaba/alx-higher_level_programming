#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2], (err, res, body) => {
  if (err) return;
  fs.writeFile(process.argv[3], body, 'utf8', err => {
    if (err) {
      console.error(err);
    }
  });
});
