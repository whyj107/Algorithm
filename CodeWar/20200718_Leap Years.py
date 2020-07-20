# 문제
# Leap Years

# 나의 풀이
def isLeapYear(year):
    return True if (year%4 == 0 and year%100 != 0) or year%400 == 0 else False

# 다른 사람의 풀이
def isLeapYear1(year):
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0

from calendar import isleap as isLeapYear2

if __name__ == '__main__':
    print(isLeapYear(1984), True)
    print(isLeapYear(2000), True)

    print(isLeapYear(1234), False)
    print(isLeapYear(1100), False)