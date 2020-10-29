# Array combinations
# https://www.codewars.com/kata/59e66e48fc3c499ec5000103/train/python

# 나의 풀이
from functools import reduce
def solve(arr):
    return reduce(lambda x, y: x*y, [len(set(i)) for i in arr])

# 다른 사람의 풀이
def solve1(arr):
    x = 1
    for a in arr:
        x *= len(set(a))
    return x

print(solve([[1, 2], [4], [5, 6]]), 4)
print(solve([[1, 2], [4, 4], [5, 6, 6]]), 4)
print(solve([[1, 2], [3, 4], [5, 6]]), 8)
print(solve([[1, 2, 3], [3, 4, 6, 6, 7], [8, 9, 10, 12, 5, 6]]), 72)