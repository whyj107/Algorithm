# Unlucky Days
# https://www.codewars.com/kata/56eb0be52caf798c630013c0/train/python

# 나의 풀이
import datetime
def unlucky_days(year):
    return sum(1 for i in range(1, 13) if datetime.datetime(year, i, 13).weekday()==4)

# 다른 사람의 풀이
def unlucky_days1(year):
    return sum(datetime.datetime(year, m, 13).weekday() == 4 for m in range(1, 13))

print(unlucky_days(1709), 2)
print(unlucky_days(1986), 1)
