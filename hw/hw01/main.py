# Devin Delfino
# COMP 398: Web Application Development
# HW_01
# Driver program for storing a Flat File Database as a Linked List

import LinkedList as LL

def main():
	filename = "states.csv"

	flatFile = LL.LinkedList()

	# ---------- Shows functionality for the POPULATE and DISPLAY functions -----------------------------
	print "\nTesting the Display function on the empty list..."
	flatFile.display() #displays an empty List

	print "\nTesting the Populate function on the empty list from the flat file database 'states.csv'..."
	flatFile.populate(filename)

	print "\nTesting the Display function on the populated list..."
	flatFile.display() # displays populated list

	# ---------------------------------------------------------------------------------------------------

	# ---------- Shows functionality for the SEARCH function -----------------------------

	print "\nTesting the Search function on 'Massachusetts'..."
	flatFile.search("Massachusetts")
	print "\nTesting the Search function on 'California'..."
	flatFile.search("California")
	print "\nTesting the Search function on 'Arizona'..."
	flatFile.search("Arizona")
	print "\nTesting the Search function on 'District of Colombia'..."
	flatFile.search("District of Columbia")

	# ---------------------------------------------------------------------------------------------------

	# ---------- Shows functionality for the APPEND function -----------------------------

	print "\nTesting the Append function by adding the District of Columbia to the list"

	print "Adding 'District of Columbia'..."

	# line taken from original flat file database
	line = "District of Columbia,601723,775.7080636,3,0.022622,0.005455,0.783959486,,4,1,0.037232,0.007363,1.058165664"
	flatFile.append(line.split(","))

	print "\nTesting the Search function on 'District of Columbia'..."
	flatFile.search("District of Columbia")

	# ---------------------------------------------------------------------------------------------------


if __name__ == '__main__':
	main()