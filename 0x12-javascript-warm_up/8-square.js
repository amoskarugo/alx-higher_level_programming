#!/usr/bin/node

const argv = process.argv;
const size = parseInt(argv[2]);

if (size) {
  for (let j = 0; j < size; j++) {
    let square = '';
    for (let i = 0; i < size; i++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
