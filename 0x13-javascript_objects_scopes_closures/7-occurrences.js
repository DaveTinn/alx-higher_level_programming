#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const numOfOccurence = {};

  list.reduce((result, element) => {
    numOfOccurence[element] = (numOfOccurence[element] || 0) + 1;
  }, numOfOccurence);

  return (numOfOccurence[searchElement] || 0);
};
