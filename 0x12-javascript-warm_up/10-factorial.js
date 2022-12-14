#!/usr/bin/node

const num = parseInt(process.argv[2]);

function fact (num) {
  if (isNaN(parseInt(num))) {
    return (1);
  } else if (num === 1) {
    return (1);
  } else {
    return (num * fact(num - 1));
  }
}

console.log(fact(num));
