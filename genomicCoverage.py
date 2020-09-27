#All functions needed to run the genomic coverage problem.

def main(readFileName, writeFileName):
	"""Main function that is called to run all the other functions
    
    Parameters
    ----------
    readFileName: string
        reads.csv
    writeFileName: string
        loci.csv
    
    Returns
    -------
    None 
    """
	visitedPositions = {}

	#PART 1: Open read file and fill dictionary with number of visits at each position
	inputFile = open(readFileName, "r")
	headerLine = True

	for currentLine in inputFile:
		if headerLine == True:
			headerLine = False
			continue	
	
		(startValue, lengthValue) = getStartAndLength(currentLine)
		populateVisitedPositions(startValue, lengthValue, visitedPositions)
		
	inputFile.close() 


	#PART 2: Open loci file in read mode and check each position with its value in visitedPositions to get coverage value
	outputReadFile = open(writeFileName, "r")

	headerLine = True
	newFileContent = "position,coverage\n"
	for currentLine in outputReadFile:

		if headerLine == True:
			headerLine = False
			continue

		position = getPosition(currentLine)

		coverage = getCoverage(position, visitedPositions)

		newLine = position + "," + coverage + "\n"
		newFileContent += newLine 

	outputReadFile.close()


	#PART 3: Open loci file in write mode and write the new content(includes coverage val) into it
	outputWriteFile = open(writeFileName, "w")
	outputWriteFile.write(newFileContent)
	outputWriteFile.close()


def getStartAndLength(currentLine):
	"""Parse and get the start and length values frrom each input line in reads.csv
    
    Parameters
    ----------
    currentLine : string
        The current line from reads.csv that is being fed into the function
    
    Returns
    -------
    (startValue, lengthValue) : (string, string)
        The start and length values in string format
    """

	#Eliminate the new line character from currentLine
	currentLine = currentLine.rstrip()

	#Split line into start and length values using the "," delimiter
	thisLine = currentLine.split(',')
	startValue = thisLine[0]
	lengthValue = thisLine[1]

	return (startValue, lengthValue)


def populateVisitedPositions(startValue, lengthValue, visitedPositions):
	"""Populates the visitedPositions dictionary given the start and length values
    
    Parameters
    ----------
    startValue : string
        Start position value
    lengthValue : string
        Length of sequence from start value 
    visitedPositions : dictionary
        Key is position and Value is number of occurrences (coverage)
    
    Returns
    -------
    visitedPositions : dictionary 
    """

	for i in range(int(lengthValue)):
		position = int(startValue) + i

		#Case 1: Position has been visited before so we increment its coverage value
		if position in visitedPositions:
			visitedPositions[position] += 1
		#Case 2: Position has not been visited before so we initialize its value in dict to 1
		else:
			visitedPositions[position] = 1

	return visitedPositions


def getPosition(currentLine):
	"""Parses and gets the position value from the current line in loci.csv
    
    Parameters
    ----------
    currentLine : string
        The current line in loci.csv
    
    Returns
    -------
    position : string 
    """

	#Eliminate the new line character from currentLine
	tempLine = currentLine.rstrip()

	#Split the line into position and coverage values using "," delimiter
	thisLine = tempLine.split(',')
	position = thisLine[0]

	return position


def getCoverage(position, visitedPositions):
	"""Gets the coverage value at a certain position by searching in the visitedPositions dictionary
    
    Parameters
    ----------
    position : string
        Position that we want to get coverage value of 
    visitedPositions : dictionary
    	Key is position and value is coverage
    
    Returns
    -------
    coverage : string 
    """

	coverage = None

	#Case 1: Position is in visitedPositions so we just get its coverage value from the dictionary
	if int(position) in visitedPositions:
		coverage = str(visitedPositions[int(position)]) 
	#Case 2: Position is NOT in visitedPositions so we set coverage to 0 since we never encountered that position
	else:
		coverage = "0"

	return coverage




