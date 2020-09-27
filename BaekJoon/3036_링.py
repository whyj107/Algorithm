# 문제
# 링
# https://www.acmicpc.net/problem/3036

# 나의 풀이
from sys import stdin
def gcd(a, b):
    return gcd(b, a%b) if a%b else b

N = int(stdin.readline())
M = list(map(int, stdin.readline().split(' ')))
for i in range(1, N):
    g = gcd(M[0], M[i])
    print(str(M[0]//g)+"/"+str(M[i]//g))