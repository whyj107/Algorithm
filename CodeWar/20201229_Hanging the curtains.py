# Hanging the curtains
# https://www.codewars.com/kata/5d532b1893309000125cc43d/train/python

# 문제가 이해가 안가는 문제다.
# 다른 사람의 풀이
from math import *
def number_of_hooks(length, maxHook):
    return length and 2**ceil( max(0, log2(length/maxHook) )) + 1

def number_of_hooks1(length, max_hook_dist):
    n = 2
    l = length
    while l > max_hook_dist:
        n += n - 1
        l = length / (n - 1)

    return n

print(number_of_hooks(200, 70), 5)
print(number_of_hooks(200, 10), 33)