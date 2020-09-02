# 문제
# 토마토
# https://www.acmicpc.net/problem/7576

# 나의 풀이
from sys import stdin
from collections import deque
def bfs(queue):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    days = -1
    while queue:
        days += 1
        for _ in range(len(queue)):
            a, b = queue.popleft()
            for i in range(4):
                x = a + dx[i]
                y = b + dy[i]
                if 0 <= x < N and 0 <= y < M and matrix[x][y]==0:
                    matrix[x][y] = matrix[a][b]+1
                    queue.append([x, y])
    for i in matrix:
        if 0 in i:
            return -1
    return days

def solution():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                queue.append([i, j])
    return bfs(queue)

M, N = map(int, stdin.readline().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, list(stdin.readline().split()))))
print(solution())