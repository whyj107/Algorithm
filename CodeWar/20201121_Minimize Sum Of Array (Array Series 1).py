# Minimize Sum Of Array (Array Series #1)
# https://www.codewars.com/kata/5a523566b3bfa84c2e00010b/train/python

# 나의 풀이
def min_sum(arr):
    arr.sort()
    sum = 0
    while arr:
        sum += arr.pop(0)*arr.pop()
    return sum

# 다른 사람의 풀이
def min_sum1(arr):
    arr = sorted(arr)
    return sum(arr[i]*arr[-i-1] for i in range(len(arr)//2))

print(min_sum([5, 4, 2, 3]), 22)
print(min_sum([12, 6, 10, 26, 3, 24]), 342)
print(min_sum([9, 2, 8, 7, 5, 4, 0, 6]), 74)