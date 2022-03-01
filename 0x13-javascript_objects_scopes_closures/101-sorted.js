#!/usr/bin/node

const dictInput = require('./101-data').dict;
const outDict = {};

for (const key in dictInput) {
	if (dictInput[key] in outDict) {
		outDict[dictInput[key]].push(key);
	} else {
		outDict[dictInput[key]] = [key];
	}
}
console.log(outDict);
