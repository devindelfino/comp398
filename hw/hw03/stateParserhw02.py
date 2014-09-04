class Node:
	""" Creates a node that has the state, info for that state and 
    a pointer to the next node


    The Node class has three methods, the init, which defines all of the
    varialbes that the node holds, the return_state, which returns the 
    name of the state at the node and lastly the return info, which returns
    informatin about the state
	"""

	def __init__(self):
		""" defines the constructor for the node class

	    has three variables state, which holds the name of the state
	    the info which holds some information about the state, and 
            next, a pointer to the next node or None
		"""
		self.state = None
		self.info = None
		self.next = None

	def  return_state(self):
		""" returns the name of the state

	    Args:
		None

	    Returns:
		A string of the name of the state
		"""
		return self.state

	def return_info(self):
		""" returns the info about a certain state

	    Args:
		None
	
	    Returns:
		a string of the info about the state
        """
		return self.info
	

class LinkedList:
	""" Creates a LinkedList that has the head of the list and the current node

    The LinkedList class has the init which defines the head and the current
    node.  This class can add a node to the end of the list with add_node 
    and can find a node by looking for the state in the list. With the 
    LinkedList you can either display the data in your linked list with each
    node on a separate line, or write the data to a text file in the same manner.
	""" 

	def __init__(self):
		""" defines the constructor for the LinkedList class

	    The two variables in the linked list are the current node, which
	    is the end of the list an the head which is the beginning of the
            list
		"""
		self.current = None
		self.head = None

	def add_node(self, state, other):
		"""
	    Adds a node to the end of the list
		
	    Adds a new node by creating a new_node with the parameters passed
	    to the funciton and then having the current node's next point to 
	    the new node and then making the current node the new node
	
	   Args:
		state: the name of the state you are creating the node for
		info: any information about that state you would like to 
		      store
	   Returns:
		nothing
		"""
		new_node = Node()
		new_node.state = state
		new_node.info = other

		if self.head == None:
			self.current = new_node
			self.head = new_node
		else:
			self.current.next = new_node
			self.current = self.current.next

	def find(self, find_state):
		"""
	    Finds a node in the linked list whose state matches find_state

	    To go through every node in the list, you start at the head
	    and see if any pointer.state matches the find_state. If it does
  	    match then return that node if you reach the end of the list 
    	    and none of the nodes in the list match find returns a string
    	    stating there is no match in the list

	    Args:
		find_state: a string of the name of the state you want
			    to find in the list

	    Returns:
		A string of either the name of the state or a message
		saing the state was not found in the linked list 
		"""
		pointer = self.head
		if pointer.state == find_state:
			return pointer.state
		else:
			while pointer.next != None:
				pointer = pointer.next
				if pointer.state == find_state:
					return pointer.state
		print "Sorry, your item was not found"
	
	def display(self):
		"""
	    Displays each member of the linked list on its own line

	    Prints out the state and then the info for each node
	    separated by a colon, with each node on its own line

	    Args:
		None
		
	    Returns:
		None
		"""
		pointer = self.head
		while pointer != None:
			print pointer.state + "\t" + pointer.info	
			pointer = pointer.next
	
	def write_to_file(self):
		"""
	    writes the linked list to a text file

	    writes the whold linked list to a text file with each
	    node on its own line and the sate and info separated
  	    by a colon
		
	   Args:
		none

	   Returns:
	 	none
		"""
		file = open("states.txt", "w")
		
		pointer = self.head
		while pointer != None:
			file.write(pointer.state + "\t" + pointer.info)	
			pointer = pointer.next

		file.close()