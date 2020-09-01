# 문제
# 가운데를 말해요
# https://www.acmicpc.net/problem/1655

# 나의 풀이
import sys
import heapq
N = int(sys.stdin.readline())
l, r = [], []
for _ in range(N):
    n = int(sys.stdin.readline())
    if len(l) == len(r): heapq.heappush(l, (-n, n))
    else: heapq.heappush(r, (n, n))

    if r and l[0][1] > r[0][1]:
        l_v = heapq.heappop(l)[1]
        r_v = heapq.heappop(r)[1]
        heapq.heappush(r, (l_v, l_v))
        heapq.heappush(l, (-r_v, r_v))
    print(l, r)
    print(l[0][1])