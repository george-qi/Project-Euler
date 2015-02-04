"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

days = [0]  # Jan 1 1901 is a Tuesday
leap_years = 0
days_30 = [4,6,9,11]
days_31 = [1,3,5,7,8,10,12]

for year in range(1901, 2001):
	# print "new year! " + str(year)
	is_leap = False
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		leap_years += 1
		is_leap = True
	for month in range(1, 13):
		if month in days_30: add = 30
		elif month in days_31: add = 31
		elif not is_leap: add = 28
		else: add = 29 
		days.append(days[len(days)-1] + add)

days.pop()  #remove 1 January 2001
print sum([1 for day in days if day % 7 == 5])
