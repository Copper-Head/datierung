LETTERS = ['d','c','b','a','g','f','e']
CENTURIES = {0:0,100:-1,200:-2,300:-3,400:-4,500:-5}

def find_letter(years, start=0, first=True, leap=False):
	if not first:
		indx = start + years
		leap_year = leap
	else:
		indx = start + years + years/4 + 1
		if not years%4:
			leap_year=True
		else:
			leap_year = False
	try:
		if leap_year:
			return LETTERS[indx-1] + LETTERS[indx]
		else:
			return LETTERS[indx]

	except IndexError:
		return find_letter(indx-7, first=False, leap=leap_year)

def narrow_to_century(year):
	tempCent = {}
	for cent in CENTURIES:
		if year-cent > 0:
			tempCent[cent] = CENTURIES[cent]
	for c in tempCent:
		if year-c == min(year-cent for cent in tempCent):
			return (tempCent[c], year-c)

