# 문제
# 숨바꼭질
# https://www.acmicpc.net/problem/1697

# 나의 풀이
from sys import stdin
from collections import deque

def next_x(nex_n, x):
    if max_N > nex_n >= 0 and (0 == visit[nex_n] or visit[nex_n] + 1 < visit[nex_n]):
        visit[nex_n] = visit[x] + 1
        queue.append(nex_n)

def solve():
    while queue:
        x = queue.popleft()
        if x == K:
            return visit[x]
        next_x(x - 1, x)
        next_x(x + 1, x)
        next_x(x * 2, x)

N, K = map(int, stdin.readline().split())
max_N = 100001
visit = [0]*max_N
queue = deque([N])
print(solve())