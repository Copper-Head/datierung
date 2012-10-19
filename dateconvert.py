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


Please keep in mind, that the only currently supported input date format is:
	DD refdate Month Year
where refdate stands for nones/ides/calendes and all the numbers are roman
numerals.

For more information about the program in general, please refer to the 
README.txt

This particular file contains two classes: Month and DateProcessor that between
them provide the functionality to convert some date from roman to conventional
format and also tell what day of the week that date corresponded to.
'''

import re # used to scanning strings 

''' to start with some constants: names of days of the week... '''
DAYS = ['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday',
		'Monday'
		]

''' dictionary of brackets used to find day of week based on sunday letter '''
BRACKETS = {(1,10):1, (2,3,11):2, (4,7): 3, (8,0):4, (9,12):5, (5,0):6, (6,0):7}

''' list of sunday letters '''
LETTERS = ['D','C','B','A','G','F','E']

''' dictionary of centuries as keys and index changes as values. for more, see
narrow_to_century() method 
'''
CENTURIES = {0:0, 100:-1, 200:-2, 300:-3, 400:-4, 500:-5, 600:-6,
		700:0, 800:-1, 900:-2, 1000:-3, 1100:-4, 1200:-5, 1300:-6,
		1400:0, 1500:-1, 1600:-2, 1700:-3, 1800:-4, 1900:-5, 2000:-6
		}

''' class for months '''
class Month:
	def __init__(self, regex, month_num, d=31):
		self.name = re.compile(regex)
		self.num = month_num
		self.lastDay = d
		self.Calends = 1
		self.Nones = 5
		self.Ides = 13
		self.check_lateness(month_num)

	def check_lateness(self, n):
		# check if month has later nones and ides dates
		if n in [3,5,7,10]:
			self.Nones, self.Ides = 7, 15
	
	def find_date(self, n, flag=None):
		# return date of month 
		# takes arabic number as argument along with flags described below
		if flag == 'c':
			return self.Calends - n+1
		elif flag == 'n':
			return self.Nones - n+1
		elif flag == 'i':
			return self.Ides - n+1
		elif flag == 'e':
			return self.lastDay - n
		else:
			print 'Invalid flag, please use c, n, e or i'
			return None

''' create instances of months '''
jan = Month('[Jj]an(uar)?y?', 1)
feb = Month('[Ff]eb(ruar)?y?', 2, d=28)
mar = Month('[Mm]ar(ch)?', 3)
apr = Month('[Aa]pr(il)?', 4, d=30)
may = Month('[Mm]ay', 5)
jun = Month('[Jj]une?', 6, d=30)
jul = Month('[Jj]uly?', 7)
aug = Month('[Aa]ug(ust)?', 8)
sept = Month('[Ss]ept(ember)?', 9, d=30)
okt = Month('[Oo][ck]t(ober)?', 10)
nov = Month('[Nn]ov(ember)?', 11, d=30)
dec = Month('[Dd]ec(ember)?', 12)

''' create regex pattern objects for calendes, nones and ides '''
calendes = re.compile('[KkCc]alende?s')
nones = re.compile('[Nn]ones')
ides = re.compile('[Ii]des')

''' put months into a list that we can loop over later '''
MONTHS = [jan, feb, mar, apr, may, jun, jul, aug, sept, okt, nov, dec]

''' Define class for processing dates. I found this necessary so as not to
initiate and pass around certain variables everytime certain methods are run
'''
class DateProcessor:
	def __init__(self, in_date):
		''' class constructor '''
		self.one = re.compile('[iI]')
		self.four = re.compile('([iI][Vv])')
		self.five = re.compile('[vV]')
		self.nine = re.compile('[iI][xX]')
		self.ten = re.compile('[Xx]')
		self.fifty = re.compile('[lL]')
		self.hundred = re.compile('[Cc]')
		self.five_hundred = re.compile('[dD]')
		self.thousand = re.compile('[mM]')
		
		in_date = in_date.split()
		self.day = self.convert_to_arab(in_date[0])
		self.cni = in_date[1]
		self.month = in_date[2]
		self.year = self.convert_to_arab(in_date[3])

	def convert_to_arab(self, roman):
		arab = 0
		''' start by finding occurences of 4 and 9 '''
		if self.four.search(roman):
			arab += 4
			roman = self.four.sub('', roman) # deleted to avoid counting it again
		if self.nine.search(roman):
			arab += 9
			roman = self.nine.sub('', roman)
			''' Then we count all the occurences of the other characters, since
			they do not overlap.
			'''
		ones = len(self.one.findall(roman))
		fives = len(self.five.findall(roman))*5
		tens = len(self.ten.findall(roman))*10
		fifties = len(self.fifty.findall(roman))*50
		hundreds = len(self.hundred.findall(roman))*100
		five_hundreds = len(self.five_hundred.findall(roman))*500
		thousands = len(self.thousand.findall(roman))*1000

		''' We then sum up all the counts and return that sum '''
		arab = arab + ones + fives + fifties + tens + hundreds + five_hundreds + thousands
		return arab
	
	def calculate_date(self):
		''' Argumentless method modifies self.day and self.month to reflect the
		conventional day and month information.
		'''
		for m in MONTHS: #loop over month objects to see which one matches 
			if m.name.search(self.month):
				outputMonth = m

		'''Having found a prelim month, we try to identify the reference date.
		'''
		if nones.search(self.cni):
			self.day = outputMonth.find_date(self.day,'n')

		elif ides.search(self.cni):
			self.day = outputMonth.find_date(self.day,'i')

		elif calendes.search(self.cni):
			self.day = outputMonth.find_date(self.day,'c')

		'''If value of day negative, go back on month and count again. '''
		if self.day < 0:
			outputMonth = MONTHS[MONTHS.index(outputMonth)-1]
			self.day = outputMonth.find_date(abs(self.day),'e')
		''' once all is set, finalize the value of self.month. '''	
		self.month = outputMonth.num


	def narrow_to_century(self):
		'''Method to tie a year value with a century and use that along with
		the year number striped of hundreds/thousands. These values are then
		used by the find_sunday_letter() method to calculate the appropriate
		sunday letter(s) for this year. '''
		tempCent = {} #temporary dict to store centuries that match 1st filter
		for cent in CENTURIES:
			if self.year-cent >= 0:
				tempCent[cent] = CENTURIES[cent]
		for c in tempCent:
			if self.year-c == min(self.year-cent for cent in tempCent):
				return (self.year-c, tempCent[c])
	
	def find_sunday_letter(self, years, start=0, first=True, leap=False):
		if not first:
			''' if this is not first run '''
			indx = start + years
			leap_year = leap
		else:
			''' if first run '''
			indx = start + years + years/4 + 1
			if not years % 4:
				''' If a leap year, counterintuitively phrased to satisfy 
				python's syntax, since we want 'years % 4' to equal 0, and this 
				is how Python checks for this.
				'''
				leap_year=True
			else:
				leap_year = False
		try:
			if leap_year:
				return LETTERS[indx-1] + LETTERS[indx]
			else:
				return LETTERS[indx]
		except IndexError:
			''' If our index value is out of range, we recursively keep 
			decreasing it by 7 (length of our week)
			'''
			return self.find_sunday_letter(indx-7, first=False, leap=leap_year)

	def find_weekday(self):
		''' Method to determine what day of the week our date was. Since this
		is a somewhat side-line feature, the method actually returns the
		weekday instead of modifying instance attributes, as the
		calculate_date() one does.
		'''
		date = self.day
		month = self.month
		cent_bracket = self.narrow_to_century()
		letter = self.find_sunday_letter(cent_bracket[0], start=cent_bracket[1])
		if len(letter) == 2: #if we have a leap year 
			if month <= 2:	#if the month is january or february
				letter = letter[0] #use first sunday letter 
			else:
				letter = letter[1]	# use second sunday letter
		''' Identify bracket number. '''
		for b in BRACKETS:
			if month in b:
				bracket_num = BRACKETS[b]
		''' Now find first member of bracket. '''
		if not bracket_num % 2: #if bracket number is even 
			firstMember = (bracket_num + 8)/2
		else:
			firstMember = (bracket_num + 1)/2
		''' Find how many columns we need to move from first bracket date. '''
		steps = date - firstMember
		if steps >= 0:
			steps = steps % 7
		else:
			steps = 7 + steps
		L = (LETTERS[4:]+LETTERS[:4])[::-1] #we reshuffle the letter list 
		weekDay = DAYS[L.index(letter) - steps]
		return weekDay

def main():
	''' Main method to be run if file invoked from command line.
	Currently takes no arguments.
	'''
	''' When creating input, please keep in mind that it must be in the format:
	DD refdate Month Year
	with refdate referring to ides/nones/calendes, all nums must be roman nums.
	'''
	#input_date = raw_input('Please enter a roman date in the following format:\
#\nDD ides/calends/nonnes MM YEAR\n')
	#input_date = 'iv calendes march MMXII' # just an example date 
	input_date = 'iv calendes march MM' # just an example date 
	DP = DateProcessor(input_date)
	DP.calculate_date()
	weekday = DP.find_weekday()
	print DP.day, DP.month, DP.year, weekday

if __name__ == '__main__':
	main()
