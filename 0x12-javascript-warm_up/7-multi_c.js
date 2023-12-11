#!/usr/bin/node

const { argv } = require('node:process');

const myNum = parseInt(argv[2]);

if (isNaN(myNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myNum; i++) {
    console.log('C is fun');
  }
}
