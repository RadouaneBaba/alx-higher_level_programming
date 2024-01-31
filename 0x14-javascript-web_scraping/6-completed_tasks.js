#!/usr/bin/node
const request = require('request');
const myUrl = process.argv[2];
request(myUrl, { json: true }, (err, res, body) => {
  if (err) return;
  const users = body.filter(user => user.completed);
  const myObj = {};
  users.forEach(user => { myObj[user.userId] ? myObj[user.userId]++ : myObj[user.userId] = 1; });
  console.log(myObj);
});
