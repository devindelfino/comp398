// Retrieve
var MongoClient = require('mongodb').MongoClient;

// Connect to the db
MongoClient.connect("ds047930.mongolab.com:47930/ddelf", function(err, db) {
  if(!err) {
    console.log("We are connected");
  }
});