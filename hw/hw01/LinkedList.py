class Node(object):
	#State object
	def __init__(self, name, pop, elect, pen, equitability, next=None):
		self.state = name
		self.population = pop
		self.electoral = elect
		self.penrose = pen
		self.equMeasure = equitability

		self.next = next

	def printNode(self):
		print "--------------------------"
		print self.state
		print "Population: " + self.population
		print "Electoral College Votes: " + self.electoral
		print "Penrose Measure: " + self.penrose
		print "Equitability Measure: " + self.equMeasure
		print "--------------------------"

class LinkedList(object):
	#List of States
	def __init__(self):
		self.size = 0
		self.head = None

	def append(self, data):
		new_node = Node(data[0], data[1], data[3], data[4], data[6])

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
			if(temp.state == query):
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
				self.append(tempData)

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

