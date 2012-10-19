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

