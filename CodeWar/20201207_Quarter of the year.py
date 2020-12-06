# Quarter of the year
# https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/train/python

# 나의 풀이
def quarter_of(month):
    return month//3 + 1 if month%3 != 0 else month//3

# 다른 사람의 풀이
def quarter_of1(month):
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4

from math import ceil
def quarter_of2(month):
    return ceil(month / 3)

def quarter_of3(n):
    return (n + 2) // 3

print(quarter_of(3), 1)
print(quarter_of(8), 3)
print(quarter_of(11), 4)