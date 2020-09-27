#Test file for my Genomic Program functions
#
import genomicCoverage as g 
#
#


def test_getStartAndLength():
	"""Tests for the getStartAndLength function"""

	#Test with start, length, and new line char
	(startValue, lengthValue) = g.getStartAndLength("101,51\n")
	assert (startValue, lengthValue) == ("101", "51")

	#Test with start and length but no new line char
	(startValue, lengthValue) = g.getStartAndLength("20,40")
	assert (startValue, lengthValue) == ("20", "40")

	#Test with just length value
	(startValue, lengthValue) = g.getStartAndLength(",11")
	assert (startValue, lengthValue) == ("", "11")

	#Test wuth just start value and new line char
	(startValue, lengthValue) = g.getStartAndLength("9,\n")
	assert (startValue, lengthValue) == ("9", "")

	#Test with just "," and new line
	(startValue, lengthValue) = g.getStartAndLength(",\n")
	assert (startValue, lengthValue) == ("", "")

	#Test with just ","
	(startValue, lengthValue) = g.getStartAndLength(",")
	assert (startValue, lengthValue) == ("", "")


def test_populateVisitedPositions():
	"""Tests for the populateVisitedPositions function"""
	visitedPositions = {}

	#First test adding values to an empty visitedPositions dictionary
	visitedPositions = g.populateVisitedPositions("10", "3", visitedPositions)
	assert visitedPositions == {10:1, 11:1, 12:1}

	#Second test of adding values to a now populated visitedPositions dictionary
	visitedPositions = g.populateVisitedPositions("11", "1", visitedPositions)
	assert visitedPositions == {10:1, 11:2, 12:1}

	#Third test of adding values to a now populated visitedPositions dictionary
	visitedPositions = g.populateVisitedPositions("13", "2", visitedPositions)
	assert visitedPositions == {10:1, 11:2, 12:1, 13:1, 14:1}

	#Fourth test of adding values to a now populated visitedPositions dictionary
	visitedPositions = g.populateVisitedPositions("8", "3", visitedPositions)
	assert visitedPositions == {8:1, 9:1, 10:2, 11:2, 12:1, 13:1, 14:1}



def test_getPosition():
	"""Tests for the getPosition function"""

	#Test with both position, coverage, and new line char
	position = g.getPosition("10,301\n")
	assert position == "10"

	#Test with just position and new line char
	position = g.getPosition("356,\n")
	assert position == "356"
	
	#Test with just position
	position = g.getPosition("1010,")
	assert position == "1010"
	
	#Test with position and coverage, but no new line char
	position = g.getPosition("74,756")
	assert position == "74"
	
	#Test with no position and just coverage and new line char
	position = g.getPosition(",30\n")
	assert position == ""

	#Test with just a "," delimiter
	position = g.getPosition(",")
	assert position == ""
	
	


def test_getCoverage():
	"""Tests for the getCoverage function""" 
	visitedPositions = {
		50: 1,
		51: 1,
		52: 1,
		53: 1,
		54: 2,
		55: 2,
		56: 3,
		57: 2,
		58: 1
	}

	#Test with a position in dict that has a coverage of 3
	coverage = g.getCoverage(56, visitedPositions)
	assert coverage == "3"

	#Test with a position in dict that has a coverage of 1
	coverage = g.getCoverage(50, visitedPositions)
	assert coverage == "1"

	#Test with a position in dict that has a coverage of 2
	coverage = g.getCoverage(54, visitedPositions)
	assert coverage == "2"

	#Test with a small position that is not in dict
	coverage = g.getCoverage(4, visitedPositions)
	assert coverage == "0"

	#Test with a large position that is not in dict
	coverage = g.getCoverage(11000, visitedPositions)
	assert coverage == "0"

	#Test with an empty dict
	coverage = g.getCoverage(58, {})
	assert coverage == "0"

	


