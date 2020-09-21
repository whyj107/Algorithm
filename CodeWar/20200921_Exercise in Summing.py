# 문제
# Exercise in Summing
# https://www.codewars.com/kata/52cd0d600707d0abcd0003eb/train/python

# 나의 풀이
# 계속 시간 초과가 난다.
from itertools import combinations
def minimum_sum(values, n):
    if len(values) == 0 or n == 0:
        return 0
    if n >= len(values):
        return sum(values)
    return min([sum(i) for i in combinations(values, n)])

def maximum_sum(values, n):
    if len(values) == 0 or n == 0:
        return 0
    if n >= len(values):
        return sum(values)
    return max([sum(i) for i in combinations(values, n)])

# 다른 사람의 풀이
def minimum_sum1(values, n):
    return sum(sorted(values)[:n])

def maximum_sum1(values, n):
    return sum(sorted(values, reverse=True)[:n])


import heapq

def minimum_sum2(values, n):
    return sum(heapq.nsmallest(n, values))

def maximum_sum2(values, n):
    return sum(heapq.nlargest(n, values))

values = [1, 2, 3, 4]
print(minimum_sum(values, 2), 3)
print(maximum_sum(values, 5), 12)