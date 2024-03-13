#!/usr/bin/node
let numOfArgs = 0;
exports.logMe = function (item) {
  console.log(`${numOfArgs++}: ${item}`);
};
