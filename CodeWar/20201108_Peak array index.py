# Peak array index
# https://www.codewars.com/kata/5a61a846cadebf9738000076/train/python

# 나의 풀이
def peak(arr):
    for idx in range(1, len(arr)):
        if sum(arr[:idx]) == sum(arr[idx+1:]):
            return idx
    return -1

# 다른 사람의 풀이
def peak1(arr):
    l = [i for i in range(len(arr) - 1) if sum(arr[:i]) == sum(arr[i + 1:])]
    return l[0] if l else -1

def peak2(arr):
    return next(iter(i for i in range(len(arr)) if sum(arr[:i]) == sum(arr[i+1:])), -1)

print(peak([1, 2, 3, 5, 3, 2, 1]), 3)
print(peak([1, 12, 3, 3, 6, 3, 1]), 2)
print(peak([10, 20, 30, 40]), -1)