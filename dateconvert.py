# This file is to convert roman numerals into arabic ones
import re

DAYS = ['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday',
		'Monday'
		]

BRACKETS = {(1,10):1, (2,3,11):2, (4,7): 3, (8,0):4, (9,12):5, (5,0):6, (6,0):7}
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
CENTURIES = {0:0,100:-1,200:-2,300:-3,400:-4,500:-5}

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
		if n in [3,5,7,10]:
			self.Nones, self.Ides = 7, 15
	
	def find_date(self, n, flag=None):
		if flag == 'c':
			return self.Calends - n+1
		elif flag == 'n':
			return self.Nones - n+1
		elif flag == 'i':
			return self.Ides - n+1
		elif flag == 'e':
			return self.lastDay - n
		else:
			print 'Invalid flag, please use c, n or i'
			return None

# create instances of this object for months, kalendes, nones and ides
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

calendes = re.compile('[KkCc]alende?s')
nones = re.compile('[Nn]ones')
ides = re.compile('[Ii]des')

# put months into a list that we can loop over later
MONTHS = [jan, feb, mar, apr, may, jun, jul, aug, sept, okt, nov, dec]

class DateProcessor:
	def __init__(self, in_date):
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
# We define our output variable
		arab = 0
# Then all of the numerals of interest
# Start by finding all the occurences of numbers 4 and 9
		if self.four.search(roman):
			arab += 4
			roman = self.four.sub('', roman)
		if self.nine.search(roman):
			arab += 9
			roman = self.nine.sub('', roman)
# Then count all of the occurences of the other characters
		ones = len(self.one.findall(roman))
		fives = len(self.five.findall(roman))*5
		tens = len(self.ten.findall(roman))*10
		fifties = len(self.fifty.findall(roman))*50
		hundreds = len(self.hundred.findall(roman))*100
		five_hundreds = len(self.five_hundred.findall(roman))*500
		thousands = len(self.thousand.findall(roman))*1000
# Sum up all of the counts and print the results
		arab = arab + ones + fives + fifties + tens + hundreds + five_hundreds + thousands
		return arab
	
	def calculate_date(self):
		for m in MONTHS:
			if m.name.search(self.month):
				outputMonth = m
		if nones.search(self.cni):
			self.day = outputMonth.find_date(self.day,'n')

		elif ides.search(self.cni):
			self.day = outputMonth.find_date(self.day,'i')

		elif calendes.search(self.cni):
			self.day = outputMonth.find_date(self.day,'c')

		if self.day < 0:
			outputMonth = MONTHS[MONTHS.index(outputMonth)-1]
			self.day = outputMonth.find_date(abs(self.day),'e')
		
		self.month = outputMonth.num


	def narrow_to_century(self):
		tempCent = {}
		for cent in CENTURIES:
			if self.year-cent > 0:
				tempCent[cent] = CENTURIES[cent]
		for c in tempCent:
			if self.year-c == min(self.year-cent for cent in tempCent):
				return (self.year-c, tempCent[c])
	
	def find_sunday_letter(self, years, start=0, first=True, leap=False):
		if not first:
# if this is not first run
			indx = start + years
			leap_year = leap
		else:
# if first run
			indx = start + years + years/4 + 1
			if not years % 4:
# if a leap year, counterintuitively phrased since we want 'years % 4' to equal
# 0, and this is a way in Python to check for this
				leap_year=True
			else:
				leap_year = False
		try:
			if leap_year:
				return LETTERS[indx-1] + LETTERS[indx]
			else:
				return LETTERS[indx]
		except IndexError:
# If our index value is out of range, we recursively keep decreasing it by
			# 7 (length of our week)
			return self.find_sunday_letter(indx-7, first=False, leap=leap_year)

	def find_weekday(self):
		date = self.day
		month = self.month
		cent_bracket = self.narrow_to_century()
		letter = self.find_sunday_letter(cent_bracket[0], start=cent_bracket[1])
		if len(letter) == 2:
			if month <= 2:
				letter = letter[0]
			else:
				letter = letter[1]
		for b in BRACKETS:
			if month in b:
				brack = BRACKETS[b]
		if not brack % 2:
			firstMember = (brack + 8)/2
		else:
			firstMember = (brack + 1)/2
		steps = date - firstMember
		if steps >= 0:
			steps = steps % 7
		else:
			steps = 7 + steps
		weekDay = DAYS[LETTERS.index(letter) - steps]
		return weekDay



def main():
	#input_date = raw_input('Please enter a roman date in the following format:\
#\nDD ides/calends/nonnes MM YEAR\n')
	input_date = 'iv calendes march MMXII'
	DP = DateProcessor(input_date)
	DP.calculate_date()
	weekday = DP.find_weekday()
	print DP.day, DP.month, DP.year, weekday
	#print DP.day, DP.month, DP.year

if __name__ == '__main__':
	main()
