# 문제
# 카드2
# https://www.acmicpc.net/problem/2164

# 나의 풀이
import sys
from collections import deque
N = int(sys.stdin.readline())
q = deque([i for i in range(1, N+1)])
while len(q) != 1:
    q.popleft()
    q.append(q.popleft())
print(q[0])