import csv



#PART 1: Open read file and fill dictionary with number of visits at each position
readFileName = "readsTest.csv"

inputFile = open(readFileName, "r")

headerLine = True
visitedPositions = {}

for currentLine in inputFile:

	if headerLine == True:
		headerLine = False
		continue

	currentLine = currentLine.rstrip()

	#Split line into start and length values
	thisLine = currentLine.split(',')
	startValue = thisLine[0]
	lengthValue = thisLine[1]

	#print('startValue: ' + startValue)
	#print('lengthValue: ' + lengthValue)
	for i in range(int(lengthValue)):
		position = int(startValue) + i
		if position in visitedPositions:
			visitedPositions[position] += 1
		else:
			visitedPositions[position] = 1

#print(visitedPositions)	
inputFile.close()






#PART 2: Open loci file and check each position with its value in visitedPositions to get coverage value
writeFileName = "lociTest.csv"

outputFile = open(writeFileName, "r+")

headerLine = True
for currentLine in outputFile:

	if headerLine == True:
		headerLine = False
		continue

	currentLine = currentLine.rstrip()
	thisLine = currentLine.split(',')
	position = thisLine[0]

	#Case 1: Position is in visitedPossibilities so we just get its coverage value
	#        from the dictionary
	

	#Case 2: Position is NOT in visitedPossibilities so we set coverage to 0 s
	#        since we never encountered that position 

outputFile.close()


