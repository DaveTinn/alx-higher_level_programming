#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const numOfOccurence = {};

  list.forEach(element => {
    numOfOccurence[element] = (numOfOccurence[element] || 0) + 1;
  });

  return numOfOccurence[searchElement] || 0;
};
