var Node = function(data){
	this.data = data;
	this.next = null;
};

var LinkedList = function(){
	this.head = null;
	this.tail = null;
	this.length = 0;
};

LinkedList.prototype.append = function(data) {

	var newnode = new Node(data);

	if(this.head === null) {
		this.head = newnode;
		this.tail = newnode;
	}
	else {
		this.tail.next = newnode;
		this.tail = newnode;
	}
	this.length++;
};

LinkedList.prototype.print = function(){
	temp = this.head;
	var buffer = "[ ";
	while(temp != null) {
		buffer += temp.data;
		buffer += " ";
		temp = temp.next;
	};
	console.log(buffer + "]");
};

LinkedList.prototype.search = function(data) {
	temp = this.head;
	while(temp != null) {
		if(temp.data == data){
			return true;
		}
		temp = temp.next;
	};
	return false;
};

LinkedList.prototype.populate = function(file_name) {
	var fs = require('fs');
	var file = fs.readFileSync(file_name);
	file = file.toString();
	file = file.split("\n");

	for(var i=0; i<file.length; i++) {
		this.append(file[i]);
	}
};

LinkedList.prototype.writeToFile = function() {
	var fout = fopen("MyList.txt", 3);
	temp = this.head;
	while(temp != null) {
		fwrite(fout, temp[i] + "\n");
		temp = temp.next;
	};
	fclose(fout);
};