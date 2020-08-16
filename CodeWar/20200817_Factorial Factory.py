# 문제
# Factorial Factory
# https://www.codewars.com/kata/528e95af53dcdb40b5000171/train/python

# 나의 풀이
def factorial(n):
    return None if n < 0 else (1 if n == 1 or n == 0 else n * factorial(n-1))

# 다른 사람의 풀이
import math
def factorial1(n):
    if n < 0:
        return None
    return math.factorial(n)

if __name__ == '__main__':
    print(factorial(2), 2)
    print(factorial(5), 120)
    print(factorial(-1), None)