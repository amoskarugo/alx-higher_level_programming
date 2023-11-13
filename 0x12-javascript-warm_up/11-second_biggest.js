#!/usr/bin/node

const argv = process.argv;
const argsLen = argv.length - 2;

if (argsLen > 0) {
  if (argsLen === 1) {
    console.log(0);
  } else {
    const numbers = argv.slice(2);
    const sortedNumbers = [...numbers].sort((a, b) => b - a);
    console.log(sortedNumbers[1]);
  }
} else {
  console.log(0);
}
