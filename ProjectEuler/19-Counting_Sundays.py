'''
1 Jan 1900 was a Monday
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import datetime

diff = (datetime.datetime(2000,12,31) - datetime.datetime(1901,1,1))
count = 0
for i in range(1,diff.days):
    xdate = (datetime.datetime(1901,1,1)+datetime.timedelta(days=i))
    if xdate.day == 1 and xdate.isoweekday()==7:
        count += 1

print(count)

