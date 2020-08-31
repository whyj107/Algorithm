# 문제
# 요세푸스 문제0
# https://www.acmicpc.net/problem/11866

# 나의 풀이
import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
q = deque([str(i) for i in range(1, N+1)])
lst = []

while q:
    q.rotate(-(K-1))
    lst.append(q.popleft())

print('<' + ', '.join(lst) + '>')