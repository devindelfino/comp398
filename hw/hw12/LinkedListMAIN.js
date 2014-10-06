// main
var fs = require('fs')
eval(fs.readFileSync('./LinkedList.js')+'');

var LL = new LinkedList()

LL.print()

console.log("Populating Linked List")

LL.populate("sample.txt")

LL.print()

if(LL.search(16)) {
	console.log(16 + " found!")
}
else {
	console.log(16 + " not found!")
}

if(LL.search(33)) {
	console.log(33 + " found!")
}
else {
	console.log(33 + " not found!")
}