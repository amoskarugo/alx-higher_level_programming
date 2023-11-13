#!/usr/bin/node

const argv = process.argv;
const numArg = parseInt(argv[2]);

if (numArg) {
  function factorial (num) {
    if (num === 1) {
      return (1);
    }
    return num * factorial(num - 1);
  }
  console.log(factorial(numArg));
} else {
  console.log(1);
}
