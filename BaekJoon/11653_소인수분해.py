# 문제
# 소인수분해
# https://www.acmicpc.net/problem/11653

# 나의 풀이
from sys import stdin
idx = 2
N = int(stdin.readline())
while N > 1:
    if N % idx == 0:
        print(idx)
        N //= idx
    else:
        idx += 1
