# Most Frequent Weekdays
# https://www.codewars.com/kata/56eb16655250549e4b0013f4/train/python

# 나의 풀이
import datetime
def most_frequent_days(year):
    t = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    s = datetime.datetime(year, 1, 1).weekday()
    e = datetime.datetime(year, 12, 31).weekday()
    return [t[i] for i in list(set([s, e]))]

# 다른 사람의 풀이
from calendar import weekday
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def most_frequent_days1(year):
    beg = weekday(year, 1, 1)
    end = weekday(year, 12, 31)
    if beg == end:
        return [week[beg]]
    else:
        if beg < end:
            return [week[beg], week[end]]
        else:
            return [week[end], week[beg]]

print(most_frequent_days(2427), ['Friday'])
print(most_frequent_days(2185), ['Saturday'])
print(most_frequent_days(1770), ['Monday'])
print(most_frequent_days(1785), ['Saturday'])
print(most_frequent_days(1984), ['Monday', 'Sunday'])
print(most_frequent_days(2000), ['Saturday', 'Sunday'])