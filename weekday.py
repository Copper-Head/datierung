'''This file contains method and vars needed to find the day of the week given
a date (in DD/MM format) and sunday letter. It might be useful to combine
the contents of this file with some other module
'''

DAYS = ['Sun', 'Sat', 'Fri', 'Thurs', 'Wed', 'Tues', 'Mon']
BRACKETS = {(1,10):1, (2,3,11):2, (4,7): 3, (8,0):4, (9,12):5, (5,0):6, (6,0):7}
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def find_weekday(date, month, letter):
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

print find_weekday(1,8,'C')
print find_weekday(22,8,'C')
print find_weekday(22,8,'BC')
print find_weekday(22,1,'BC')

