#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
  const Occurences = dict[key];
  newDict[Occurences] = [];
  for (const value in dict) {
    if (dict[value] === Occurences) {
      newDict[Occurences].push(value);
    }
  }
}
console.log(newDict);
