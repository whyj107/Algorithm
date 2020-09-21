# 문제
# Two Sum
# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python

# 나의 풀이
from itertools import combinations
def two_sum(numbers, target):
    for i, j in combinations(numbers, 2):
        if i+j == target:
            return [numbers.index(i), numbers.index(j)] if i != j else [numbers.index(i), numbers[numbers.index(i)+1:].index(j)+numbers.index(i)+1]

# 다른 사람의 풀이
def two_sum1(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]

print(sorted(two_sum([1, 2, 3], 4)), [0, 2])
print(sorted(two_sum([1234, 5678, 9012], 14690)), [1, 2])
print(sorted(two_sum([2, 2, 3], 4)), [0, 1])