class Node(object):
	"""Stores a single database entry.

	Represents a database entry within a linked list. Specified to 
	store a name and abbreviation of a USA Territory as cargo.

	Attributes:
       name = the name of the state
       abbreviation = the postal abbreviation
       next = the next node object in the linked list
	"""	

	def __init__(self, name, abb, next=None):
		"""Initializes Node class with territory name and postal abbreviation."""

		self.name = name
		self.abbreviation = abb
		self.next = next

	def printNode(self):
		"""Displays cargo of a Node object.

		Args:
			None

		Returns:
			None
		"""

		print "--------------------------"
		print "State/Territory: " + self.name
		print "Abbreviation: " + self.abbreviation.rstrip()
		print "--------------------------"

class LinkedList(object):
	"""Stores an entire flat file database in the form of Node objects.

	Uses Node objects to store a flat file database. Specified to store
	the flat file database containing USA Territory names and abbreviations.

	Attributes:
		size = the number of entries within the Linked List
		head = the first entry (Node object) in the Linked List
	"""

	def __init__(self):
		"""Initializes LinkedList class by setting the size as 0 and the head Node to None."""

		self.size = 0
		self.head = None

	def append(self, n, a):
		"""Appends a new Node object to the end of the Linked List instance.

		Creates a new instance of the Node class and inserts it at the very end
		of the Linked List instance.

		Args:
			n = the name of the territory/state
			a = the postal abbreviation of the territory/state

		Returns:
			None
		"""

		new_node = Node(n, a)

		if(self.head == None):
			self.head = new_node
		else:
			temp = self.head

			while(temp.next != None):
				temp = temp.next

			temp.next = new_node

	def search(self, query):
		"""Searches for a specific query in the linked list

		Iterates through the entries in the linked list for a specific query.
		Prints out the entry if it is found.

		Args:
			query = the name of the state/territory that is being searched for

		Returns:
			A Boolean, True  - the search item was found
					   False - the search item was not found
		"""

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
		"""Populates an empty linked list with a flat file database

		Only populates an empty linked list.

		Args:
			filename = the name of the file that is to be read into the linked list

		Returns:
			A Boolean, True  - the search item was found
					   False - the search item was not found
		"""

		if(self.head != None):
			print "This Linked List is already populated. Please try again with an empty list."
		else:
			f = open(filename, "r")
			for entry in f:
				tempData = entry.split(",")
				self.append(tempData[0], tempData[1])

			f.close()

	def display(self):
		"""Displays each entry within the linked list 

		Args:
			None

		Returns:
			None
		"""

		if(self.head == None):
			print "\n\n--------------------------"
			print "This Linked List is empty."
			print "--------------------------\n\n"
		else:
			temp = self.head
			while(temp != None):
				temp.printNode();
				temp = temp.next

