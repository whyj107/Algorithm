# 문제
# 최대 힙
# https://www.acmicpc.net/problem/11279

# 나의 풀이
import sys
import heapq
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(lst, (-n))
    else:
        try:
            print(-1*heapq.heappop(lst))
        except:
            print(0)