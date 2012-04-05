Letters = ['d','c','b','a','g','f','e']

def find_letter(years, start=0, first=True, schalt=False):
	if not first:
		indx = start + years
		schlt_yr = schalt
	else:
		indx = start + years + years/4 + 1
		if not years%4:
			schlt_yr=True
		else:
			schlt_yr = False
	try:
		if schlt_yr:
			return Letters[indx-1] + Letters[indx]
		else:
			return Letters[indx]

	except IndexError:
		return find_letter(indx-7, first=False, schalt=schlt_yr)

#print find_letter(0)
#print find_letter(12)
#print find_letter(16)
#print find_letter(20)
#print find_letter(24)
#print find_letter(99)


CENTURIES = {0:0,100:-1,200:-2,300:-3,400:-4,500:-5}

def narrow_to_century(year):
	tempCent = {}
	for cent in CENTURIES:
		if year-cent > 0:
			tempCent[cent] = CENTURIES[cent]
	print tempCent
	for c in tempCent:
		if year-c == min(year-cent for cent in tempCent):
			print c
			return (tempCent[c], year-c)

n = narrow_to_century(499)
print n
print find_letter(n[1], start=n[0])
