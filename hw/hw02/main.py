# State Abbreviation

import linked_list

def main():
	file_name = "territories.csv"

	flat_file = linked_list.LinkedList()

	# ---------- Shows functionality for the POPULATE and DISPLAY functions -----------------------------

	print "\nTesting the Display function on the empty list..."
	flat_file.display() 

	print "\nTesting the Populate function on the empty list from the flat file database 'territories.csv'..."
	flat_file.populate(file_name)

	print "\nTesting the Display function on the populated list..."
	flat_file.display()

	# ---------------------------------------------------------------------------------------------------

	# ---------- Shows functionality for the SEARCH function -----------------------------

	print "\nTesting the Search function on 'Massachusetts'..."
	flat_file.search("Massachusetts")

	print "\nTesting the Search function on 'California'..."
	flat_file.search("California")

	print "\nTesting the Search function on 'Arizona'..."
	flat_file.search("Arizona")

	print "\nTesting the Search function on 'District of Colombia'..."
	flat_file.search("District of Columbia")

	# ---------------------------------------------------------------------------------------------------

if __name__ == '__main__':
	main()