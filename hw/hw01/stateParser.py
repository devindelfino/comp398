def main():

	states = {}
	f = open("Sheet1.csv","r")

	for line in f:
		temp = line.split(",")


		states[temp[0]] = {"Population" : temp[1],
		"SquareRoot of Pop" : temp[2],
		"Electoral College" : temp[3],
		"Penrose" : temp[4],
		"Banzhaf" : temp[5],
		"Equitability Measure" : temp[6],
		"weightRatio" : temp[7],
		"New Electoral College" : temp[8],
		"deltaWeight" : temp[9],
		"New Penrose" : temp[10],
		"New Bhanzaf" : temp[11],
		"New Equitability" : temp[12]}

	f.close()
	for s in states:
		print s + " " + states[s]["Population"]



if __name__ == '__main__':
	main()