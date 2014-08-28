# State Abbreviation

import LinkedListAbb as LL

def main():
	filename = "territories.csv"

	flatFile = LL.LinkedList()

	# ---------- Shows functionality for the POPULATE and DISPLAY functions -----------------------------
	print "\nTesting the Display function on the empty list..."
	flatFile.display() #displays an empty List

	print "\nTesting the Populate function on the empty list from the flat file database 'territories.csv'..."
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

if __name__ == '__main__':
	main()