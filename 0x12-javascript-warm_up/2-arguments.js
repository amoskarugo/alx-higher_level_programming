#!/usr/bin/node

const argv = process.argv;
// const arguments = argv.slice(2);
const numberOfArgs = argv.length - 2;

if (numberOfArgs === 0) {
  console.log('No argument');
} else if (numberOfArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
