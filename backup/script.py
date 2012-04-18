# this file contains scripts used to create the tables that are used in the
# main program. This file is essentially kept only so that the tables can be
# reproduced or recreated/redone

LETTERS = ['d','c','b','a','g','f','e']
counter = 0
table = {}

def assign_letter(year, schalt, counter, let=LETTERS):
	answer = ''
	if schalt:
		schalt = False
		ans = assign_letter(year, schalt, counter)
		answer = ''.join([ans[0], let[ans[1]]])
		if (ans[1] + 1) == len(let):
			counter = 0
		else:
			counter = ans[1]+1
	else:
		answer = ''.join([answer, let[counter]])
		if (counter + 1) == len(let):
			counter = 0
		else:
			counter += 1
	return (answer, counter)

for cent in range(0,2001,100):
	for year in range(100):
		schalt = False
		if year%4 == 0:
			schalt = True
		x = assign_letter(year, schalt, counter)
		table[cent+year] = x[0]
		counter = x[1]
print table
