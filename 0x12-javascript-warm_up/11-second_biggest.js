#!/usr/bin/node

const { argv } = require('process');

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  let biggest = parseInt(argv[2]);
  let secBiggest = parseInt(argv[2]);
  let index = 2;
  for (let i = 3; i < argv.length; i++) {
    if (parseInt(argv[i]) > biggest) {
      biggest = parseInt(argv[i]);
      index = i;
    }
  }
  if (secBiggest === biggest) {
    secBiggest = parseInt(argv[3]);
  }
  for (let i = 3; i < argv.length; i++) {
    if (i == index) {
      continue;
    }
    if (parseInt(argv[i]) > secBiggest) {
      secBiggest = parseInt(argv[i]);
    }
  }
  console.log(secBiggest);
}
