class Node(object):
	#State object
	def __init__(self, name, abb, next=None):
		self.name = name
		self.abbreviation = abb
		self.next = next

	def printNode(self):
		print "--------------------------"
		print "State/Territory: " + self.name
		print "Abbreviation: " + self.abbreviation
		print "--------------------------"

class LinkedList(object):
	#List of States
	def __init__(self):
		self.size = 0
		self.head = None

	def append(self, n, a):
		new_node = Node(n, a)

		if(self.head == None):
			self.head = new_node
		else:
			temp = self.head

			while(temp.next != None):
				temp = temp.next

			temp.next = new_node

	def search(self, query):
		
		temp = self.head
		while(temp != None):
			if(temp.name == query):
				print query + " found!"
				temp.printNode()
				return True
			temp = temp.next

		print query + " NOT found!"
		return False


	def populate(self, filename):
		# Only a completely empty Linked List can be populated
		if(self.head != None):
			print "This Linked List is already populated. Please try again with an empty list."
		else:
			f = open(filename, "r")
			for entry in f:
				tempData = entry.split(",")
				self.append(tempData[0], tempData[1])

			f.close()

	def display(self):
		if(self.head == None):
			print "\n\n--------------------------"
			print "This Linked List is empty."
			print "--------------------------\n\n"
		else:
			temp = self.head
			while(temp != None):
				temp.printNode();
				temp = temp.next

