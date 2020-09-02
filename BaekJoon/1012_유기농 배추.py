# 문제
# 유기농 배추
# https://www.acmicpc.net/problem/1012

# 나의 풀이
from sys import stdin

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(i, j):
    queue = [[i, j]]
    matrix[i][j] = 0
    cnt_ = 1
    while queue:
        a, b = map(int, queue.pop(0))
        for k in range(4):
            x = a+dx[k]
            y = b+dy[k]
            if 0 <= x < M and 0 <= y < N and matrix[x][y] == 1:
                matrix[x][y] = 0
                queue.append([x, y])
                cnt_ += 1
    cnt.append(cnt_)

import pprint
T = int(stdin.readline())
for _ in range(T):
    M, N, K = map(int, stdin.readline().split())
    matrix = [[0]*(N+1) for _ in range(M+1)]
    for i in range(K):
        x, y = map(int, stdin.readline().split())
        matrix[x][y] = 1
    # pprint.pprint(matrix)
    cnt = []
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1: bfs(i, j)
    print(len(cnt))