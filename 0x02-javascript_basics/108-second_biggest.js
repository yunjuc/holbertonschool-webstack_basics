#!/usr/bin/node
const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  args.sort();
  console.log(args[args.length - 2]);
}
