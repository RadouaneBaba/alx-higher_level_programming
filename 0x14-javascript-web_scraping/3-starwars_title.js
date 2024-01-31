#!/usr/bin/node
const request = require('request');
const myPath = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(myPath, { json: true }, (err, res, body) => {
  if (err) return;
  console.log(body.title);
});
