# 문제
# 회전하는 큐
# https://www.acmicpc.net/problem/1021

# 풀이
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
lst = deque(list(map(int, sys.stdin.readline().split())))
q = deque([i for i in range(1, N+1)])
cnt = 0
for i in lst:
    j = 0
    while i != q[j]:
        j += 1
    j = len(q) - j if len(q) - j < j else - j
    q.rotate(j)
    cnt += abs(j)
    q.popleft()
print(cnt)