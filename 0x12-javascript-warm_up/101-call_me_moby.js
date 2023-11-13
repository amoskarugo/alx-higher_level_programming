#!/usr/bin/node

exports.callMeMoby = function (x, func) {
  while (x) {
    func();
    x--;
  }
};
