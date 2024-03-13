#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((result, element) => element === searchElement ? result + 1 : result, 0);
};
