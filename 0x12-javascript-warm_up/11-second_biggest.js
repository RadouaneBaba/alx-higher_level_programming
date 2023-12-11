#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  let biggest = parseInt(argv[2]);
  let secBiggest = parseInt(argv[2]);
  for (let i = 3; i < argv.length; i++) {
    if (parseInt(argv[i]) > biggest) {
      secBiggest = biggest;
      biggest = parseInt(argv[i]);
    }
  }
  console.log(secBiggest);
}
