import stateParserhw02

def main():

# 1. Creating an empty Linked List
	linked_list = stateParserhw02.LinkedList()

# 2. Adding a single Node to Linked List
	linked_list.add_node( "States", "Population" )
	
# 3. Populating LinkedList with data collected from class
	f = open("Sheet1hw02.csv","r")

	for line in f:
		temp = line.split(",")

		
		s = temp[0]
		i = "Population : " + temp[1]
#		"SquareRoot of Pop" : temp[2],
#		"Electoral College" : temp[3],
#		"Penrose" : temp[4],
#		"Banzhaf" : temp[5],
#		"Equitability Measure" : temp[6],
#		"weightRatio" : temp[7],
#		"New Electoral College" : temp[8],
#		"deltaWeight" : temp[9],
#		"New Penrose" : temp[10],
#		"New Bhanzaf" : temp[11],
#		"New Equitability" : temp[12]}

		linked_list.add_node(s, i)

	f.close()
	
# 4. Searching for "Texas" in LinkedList
	print linked_list.find("Texas")

# 5. Displaying LinkedList
#	linked_list.display()

# 6. Write data to textfile
	linked_list.write_to_file()


if __name__ == '__main__':
	main()