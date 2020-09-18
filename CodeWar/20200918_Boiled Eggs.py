# 문제
# Boiled Eggs
# https://www.codewars.com/kata/52b5247074ea613a09000164/train/python

# 나의 풀이
def cooking_time(eggs):
    return (eggs//8)*5 if eggs%8 == 0 else (eggs//8+1)*5

# 다른 사람의 풀이
from math import *
def cooking_time1(eggs):
    return 5*ceil(eggs/8.0)

print(cooking_time(0), 0)
print(cooking_time(5), 5)
print(cooking_time1(10), 10)