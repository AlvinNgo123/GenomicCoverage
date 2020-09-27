



def main(readFileName, writeFileName):
	visitedPositions = {}

	#PART 1: Open read file and fill dictionary with number of visits at each position
	inputFile = open(readFileName, "r")
	headerLine = True

	for currentLine in inputFile:
		if headerLine == True:
			headerLine = False
			continue	
		'''currentLine = currentLine.rstrip()
		#Split line into start and length values
		thisLine = currentLine.split(',')
		startValue = thisLine[0]
		lengthValue = thisLine[1]'''
		(startValue, lengthValue) = getStartAndLength(currentLine)
		'''for i in range(int(lengthValue)):
			position = int(startValue) + i
			if position in visitedPositions:
				visitedPositions[position] += 1
			else:
				visitedPositions[position] = 1'''
		populateVisitedPositions(startValue, lengthValue, visitedPositions)
		
	inputFile.close()


	#PART 2: Open loci file in read mode and check each position with its value in visitedPositions to get coverage value
	outputReadFile = open(writeFileName, "r")

	headerLine = True
	newFileContent = ""
	for currentLine in outputReadFile:

		if headerLine == True:
			headerLine = False
			continue

		'''tempLine = currentLine.rstrip()
		thisLine = tempLine.split(',')
		position = thisLine[0]'''
		position = getPosition(currentLine)

		'''#Case 1: Position is in visitedPositions so we just get its coverage value
		#        from the dictionary
		if int(position) in visitedPositions:
			thisLine[1] = str(visitedPositions[int(position)]) 
		#Case 2: Position is NOT in visitedPositions so we set coverage to 0 s
		#        since we never encountered that position
		else:
			thisLine[1] = "0"'''
		coverage = getCoverage(position, visitedPositions)

		newLine = position + "," + coverage + "\n"
		newFileContent += newLine 

	outputReadFile.close()


	#PART 3: Open loci file in write mode and write the new content(includes coverage val) into it
	outputWriteFile = open(writeFileName, "w")
	outputWriteFile.write(newFileContent)
	outputWriteFile.close()





def getStartAndLength(currentLine):
	#Eliminate the new line character from currentLine
	currentLine = currentLine.rstrip()

	#Split line into start and length values using the "," delimiter
	thisLine = currentLine.split(',')
	startValue = thisLine[0]
	lengthValue = thisLine[1]

	return (startValue, lengthValue)


def populateVisitedPositions(startValue, lengthValue, visitedPositions):
	for i in range(int(lengthValue)):
		position = int(startValue) + i

		if position in visitedPositions:
			visitedPositions[position] += 1
		else:
			visitedPositions[position] = 1


def getPosition(currentLine):
	#Eliminate the new line character from currentLine
	tempLine = currentLine.rstrip()

	#Split the line into position and coverage values using "," delimiter
	thisLine = tempLine.split(',')
	position = thisLine[0]

	return position


def getCoverage(position, visitedPositions):
	coverage = None

	#Case 1: Position is in visitedPositions so we just get its coverage value
	#        from the dictionary
	if int(position) in visitedPositions:
		coverage = str(visitedPositions[int(position)]) 
	#Case 2: Position is NOT in visitedPositions so we set coverage to 0 s
	#        since we never encountered that position
	else:
		coverage = "0"

	return coverage

main("reads.csv", "loci.csv")


