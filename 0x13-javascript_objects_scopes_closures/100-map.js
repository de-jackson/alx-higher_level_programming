#!/usr/bin/node

const myList = require('./100-data').list;
const mapList = myList.map((num, index) => num * index);
console.log(myList);
console.log(mapList);
