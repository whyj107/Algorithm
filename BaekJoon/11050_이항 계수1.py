# 문제
# 이항 계수1
# https://www.acmicpc.net/problem/11050

# 나의 풀이
def fact(n):
    return 1 if n == 0 else n*fact(n-1)

from sys import stdin
n1, n2 = map(int, stdin.readline().split(' '))
print(fact(n1)//(fact(n2)*fact(n1-n2)))