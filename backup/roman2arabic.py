'''
Datierung. 
An exercise in Python. Converts Latin dates found in medieval chronicles
and documents into conventional format.

Copyright (C) 2012  Ilia Kurenkov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

For questions feel free to email me:
ilia kurenkov at gmail
'''

# This file is to convert roman numerals into arabic ones
import re
# We ask for a roman numeral (first way of getting a numeral)
# Then the numeral is set to lower case, for ease of analysis
#num = raw_input("Please give a roman numeral \n")
#num = num.lower()

# A function that calculates the answer
def convert(roman):
# We define our output variable
	arab = 0

# Then all of the numerals of interest
	one = re.compile('i')
	four = re.compile('iv')
	five = re.compile('v')
	nine = re.compile('ix')
	ten = re.compile('x')
	fifty = re.compile('l')
	hundred = re.compile('c')
	five_hundred = re.compile('d')
	thousand = re.compile('m')

# Start by finding all the occurences of numbers 4 and 9
	if four.search(roman) != None:
		arab += 4
		roman = roman.replace(four.pattern, '')
	if nine.search(roman) != None:
		arab += 9
		roman = roman.replace(nine.pattern, '')

# Then count all of the occurences of the other characters
	ones = len(one.findall(roman))
	fives = len(five.findall(roman))*5
	tens = len(ten.findall(roman))*10
	fifties = len(fifty.findall(roman))*50
	hundreds = len(hundred.findall(roman))*100
	five_hundreds = len(five_hundred.findall(roman))*500
	thousands = len(thousand.findall(roman))*1000

# Sum up all of the counts and print the results
	arab = arab + ones + fives + fifties + tens + hundreds + five_hundreds + thousands
	return arab

# We then print a test run of the function
#print convert(num)
