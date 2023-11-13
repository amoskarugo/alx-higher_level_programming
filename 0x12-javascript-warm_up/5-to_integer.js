#!/usr/bin/node

const argv = process.argv;
const number = parseInt(argv[2]);

if (number) {
  console.log(number);
} else {
  console.log('Not a number');
}
