#!/usr/bin/node

const argv = process.argv;
let occurrences = parseInt(argv[2]);

if (occurrences) {
  while (occurrences > 0) {
    console.log('C is fun');
    occurrences--;
  }
} else {
  console.log('Missing number of occurrences');
}
