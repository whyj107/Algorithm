# 문제
# 절댓값 힙
# https://www.acmicpc.net/problem/11286

# 나의 풀이
import sys
import heapq
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(heap, (abs(n), n))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
    print(heap)