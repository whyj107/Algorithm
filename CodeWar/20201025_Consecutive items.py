# Consecutive items
# https://www.codewars.com/kata/5f6d533e1475f30001e47514/train/python

# 나의 풀이
def consecutive(arr, a, b):
    return True if abs(arr.index(a) - arr.index(b)) == 1 else False

# 다른 사람의 풀이
def consecutive1(A, a, b):
    return abs(A.index(a)-A.index(b))==1

print(consecutive([1, 3, 5, 7], 3, 7), False)
print(consecutive([1, 3, 5, 7], 3, 1), True)
print(consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4), True)