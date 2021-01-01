# Coprime Validator
# https://www.codewars.com/kata/585c50e75d0930e6a7000336/train/python

# 최대 공약수를 구해서 최대공약수가 1이면 True 아니면 False를 리턴한다.

# 나의 풀이
def gcd_(p, q):
    if q == 0: return p
    return gcd_(q, p % q)

def are_coprime(n, m):
    return gcd(n, m) == 1

# 다른 사람의 풀이
from fractions import gcd
def are_coprime1(n, m):
  return gcd(n, m) == 1

def are_coprime(n, m):
    while m > 0:
        n, m = m, n % m
    return n == 1

print(are_coprime(20, 27), True)
print(are_coprime(12, 39), False)