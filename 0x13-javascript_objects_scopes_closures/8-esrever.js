#!/usr/bin/node

exports.esrever = function (list) {
  let temp;
  for (let i = 0; i < (list.length / 2); i++){
    temp = list[i];
    list[i] = list[list.length - i];
    list[list.length - i] = temp;
  }
  return list;
};
