class Node(object):
	"""Stores a single database entry.

	Represents a database entry within a linked list.
	Specified to store a state's name, population, electoral votes,
	penrose measure, and equitability measure as cargo.

	Attributes:
       state = the name of the state
       population = the population of the state
       electoral = the number of electoral college Votes
       penrose = the penrose measure (absolute voting power)
       equMeasure = the equitability measure (measure of fairness)
       next = the next node object in the linked list
	"""
	
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
	"""Stores an entire flat file database in the form of Node objects.

	Uses Node objects to store a flat file database. This Linked List class is 
	specified to store the flat file database containing USA Territory names and abbreviations.

	Attributes:
		size = the number of entries within the Linked List
		head = the first entry (Node object) in the Linked List
	"""

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

