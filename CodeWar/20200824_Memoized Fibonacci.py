# 문제
# Memoized Fibonacci
# https://www.codewars.com/kata/529adbf7533b761c560004e5/train/python

# 나의 풀이
# 속도 실패
def fibonacci1(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

f = {}
def fibonacci2(n):
    if n in f:
        return f[n]
    else:
        f[n] = n if n < 2 else fibonacci(n-2) + fibonacci(n-1)
        return f[n]

# 다른 사람의 풀이
from functools import lru_cache
@lru_cache(None)
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    print(fibonacci(70), 190392490709135)
    print(fibonacci(60), 1548008755920)
    print(fibonacci(50), 12586269025)