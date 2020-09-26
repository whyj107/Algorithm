# 문제
# 검문
# https://www.acmicpc.net/problem/2981

# 풀이
from sys import stdin
N = int(stdin.readline())
M = [int(stdin.readline()) for i in range(N)]
M.sort()

tmp = M[-1] - M[0]

y = []
for i in range(2, int(tmp**0.5)+1):
    if tmp % i == 0:
        y.append(i)
        if tmp//i not in y: y.append(tmp//i)
y.sort()
y.append(tmp)
for i in y:
    for n in range(N):
        if n == N-1:
            print(i, end=" ")
        elif M[n] % i != M[n+1] % i:
            break

# 다른 사람의 풀이
"""
import sys
input = sys.stdin.readline

def gcd(a, b):
    return gcd(b, a % b) if a % b else b

n = int(input())
num = sorted([int(input()) for _ in range(n)])

get = num[1] - num[0]
for i in range(2, n):
    get = gcd(get, num[i]-num[i-1])

res = set()
for i in range(2, int(get**0.5)+1):
    if get % i == 0:
        res.add(i)
        res.add(get//i)
res.add(get)
res = sorted(list(res))
print(' '.join(map(str, res)))
"""