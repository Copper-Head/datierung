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
