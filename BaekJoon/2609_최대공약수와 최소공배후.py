# 문제
# 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609

# 나의 문제
# 최대공약수
def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

# 최소공배수
def lcm(a, b):
    return a*b//gcd(a, b)

from sys import stdin
a, b = map(int, stdin.readline().split(' '))
print(gcd(a, b))
print(lcm(a, b))