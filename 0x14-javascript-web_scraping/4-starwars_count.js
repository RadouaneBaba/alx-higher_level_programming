#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const chaUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
const options = { json: true };

request(url, options, (err, res, body) => {
  if (err) return;
  try {
    const myArr = body.results.filter(a => a.characters.includes(chaUrl));
    console.log(myArr.length);
  } catch (err) {
    console.log(err);
  }
});
