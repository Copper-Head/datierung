import re
import sys
from roman2arabic import convert

# define useful container object
class Month:
	def __init__(self, regex, num, d=31):
		self.name = re.compile(regex)
		self.num = num
		self.lastDay = d
		self.Calends = 1
		self.Nones = 5
		self.Ides = 13
		self.check_lateness(num)

	def check_lateness(self, n):
		late = [3,5,7,10]
		if n in late:
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

_30_days = [4,6,9,11]

# define the output variables
monthNum = 0
outputDate = 0

#initialize input variable with a request to user
inputDate = raw_input('Name a roman date \n')

for m in MONTHS:
	if m.name.search(inputDate):
		monthNum = m.num
		outputMonth = m
		inputDate = m.name.sub('', inputDate)
	# below is work in progress, an exit case, if we dont find any months in
	# inputDate
	#else:
		#print 'no month found'
		#continue
		#sys.exit()

if nones.search(inputDate):
	inputDate = nones.split(inputDate)
	Date = convert(inputDate[0])
	outputDate = outputMonth.find_date(Date,'n')

elif ides.search(inputDate):
	inputDate = ides.split(inputDate)
	Date = convert(inputDate[0])
	outputDate = outputMonth.find_date(Date,'i')

elif calendes.search(inputDate):
	inputDate = calendes.split(inputDate)
	Date = convert(inputDate[0])
	outputDate = outputMonth.find_date(Date,'c')

if outputDate < 0:
	monthNum -= 1
	outputMonth = MONTHS[monthNum-1]
	outputDate = outputMonth.find_date(abs(outputDate),'e')

#print outputDate, monthNum, convert(inputDate[1])
