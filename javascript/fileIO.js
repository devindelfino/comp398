var fs = require('fs')
var file = fs.readFileSync(process.argv[2])
file = file.toString()
file = file.split('\n')
console.log((file.length)-1)