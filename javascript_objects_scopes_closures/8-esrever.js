#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  const len = list.length;
  for (let i = len - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
