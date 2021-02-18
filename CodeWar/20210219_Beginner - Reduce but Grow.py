# Beginner - Reduce but Grow
# https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python

# 나의 풀이
def grow0(arr):
    result = 1
    for n in arr:
        result *= n
    return result

from functools import reduce
def grow(arr):
    return reduce((lambda x, y: x*y), arr)

tests = [
    [6, [1, 2, 3]],
    [16, [4, 1, 1, 1, 4]],
    [64, [2, 2, 2, 2, 2, 2]],
]

for exp, inp in tests:
    print(grow(inp), exp)