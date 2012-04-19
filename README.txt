*********** README file **********

N.B.DESCRIPTION
This is a "baby" date converter program written by Ilia Kurenkov
(ilia.kurenkov@gmail.com) as an excercise in python. As such it can be 
considered free software licensed under the GPL.

I got the idea for this program while doing a homework assignment for a 
medieval history class at the University of Konstanz.
I noticed that we used a series of tables to figure out what the modern date
format of the dates we encountered in chronics and documents for the course.

These tables can be found at this link (N.B. webpage in German):
http://www.adfontes.uzh.ch/1001.php

The website will ask for a login, feel free to just use my first and last name
for the ID and password respectively (both should be capitalized). No personal
information will be compromised, because you will only have (relatively)
anonymous access to the website. Once logged in, click on the tab 'Resoursen',
then on the link 'Datierung Auflösen'.


Seeing as the program was first and foremost an excercise, it only processes
input dates given in certain formats and does only a limited number of
operations with them. The only currently acceptable format for a date is the
following (all numerals should be roman):

dd refdate month year

where refdate stands for nones/ides/calendes type of reference date.
The years currently covered are 0-2099.

Another thing to keep in mind is that this program accepts a mixture of
roman-style month names along with English and even German month names. 
It also only deals with Julian/Gregorian month names, pre-Julian roman dates
are currently not supported.

Things that I would like to add to this system:
	- support B.C. dates as well as A.D.
	- support for different input formats including partial date entries
	- support for various kinds of roman calendars (pre/post-Numa reform)
	- support for greek calendar
	- [ambitious] capability to extract dates from text and convert them
	

Known Bugs:
Currently, if we run the find_weekday() method without first running the
calculate_date() one we will be using the original input values for self.day
and self.month, which could be different from their actual value, since they
often get changed as part of the date calculation process.
At this point in time this is not exactly a program, more a collection of files
and modules that I plan to combine later on. The purpose of this program [in
the future] is to find instances of roman/medieval dates in documents and
convert them into conventional dates.


SYSTEM REQUIREMENTS
All of the files in this program were created using Python 2.7.
No modules or methods are used that are very unique or specific to that version
of Python, so everything should work fine on any installation of Python on any
machine.
