# Doubleton number
# https://www.codewars.com/kata/604287495a72ae00131685c7/train/python

# 나의 풀이
def doubleton(num):
    while num:
        num += 1
        if len(set(str(num))) == 2:
            return num

# 다른 사람의 풀이
from itertools import count
def doubleton1(num):
    return next(n for n in count(num+1) if len(set(str(n))) == 2)

print(doubleton(120), 121)
print(doubleton(1234), 1311)
print(doubleton(10), 12)
print(doubleton(1), 10)
print(doubleton(111), 112)