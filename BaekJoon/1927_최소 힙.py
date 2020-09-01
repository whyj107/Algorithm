# 문제
# 최소 힙
# https://www.acmicpc.net/problem/1927

# 나의 풀이
import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(heap, n)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)