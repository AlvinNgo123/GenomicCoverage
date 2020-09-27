
#PART 1: Open read file and fill dictionary with number of visits at each position
readFileName = "reads.csv"

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






#PART 2: Open loci file in read mode and check each position with its value in visitedPositions to get coverage value
writeFileName = "loci.csv"

outputReadFile = open(writeFileName, "r")

headerLine = True
newFileContent = ""
for currentLine in outputReadFile:

	if headerLine == True:
		headerLine = False
		continue

	tempLine = currentLine.rstrip()
	#print(currentLine)
	thisLine = tempLine.split(',')
	position = thisLine[0]

	#Case 1: Position is in visitedPositions so we just get its coverage value
	#        from the dictionary
	if int(position) in visitedPositions:
		thisLine[1] = str(visitedPositions[int(position)]) 
	#Case 2: Position is NOT in visitedPositions so we set coverage to 0 s
	#        since we never encountered that position
	else:
		thisLine[1] = "0"

	newLine = thisLine[0] + "," + thisLine[1] + "\n"
	newFileContent += newLine 
outputReadFile.close()



#PART 3: Open loci file in write mode and write the new content(includes coverage val) into it
outputWriteFile = open(writeFileName, "w")
outputWriteFile.write(newFileContent)
outputWriteFile.close()


