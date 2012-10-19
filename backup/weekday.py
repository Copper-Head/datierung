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


This file contains method and vars needed to find the day of the week given
a date (in DD/MM format) and sunday letter. It might be useful to combine
the contents of this file with some other module
'''

DAYS = ['Sun', 'Sat', 'Fri', 'Thurs', 'Wed', 'Tues', 'Mon']
BRACKETS = {(1,10):1, (2,3,11):2, (4,7): 3, (8,0):4, (9,12):5, (5,0):6, (6,0):7}
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
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

def main():
	pass

if __name__ == '__main__':
	main()
