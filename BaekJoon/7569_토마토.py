# 문제
# 토마토
# https://www.acmicpc.net/problem/7569

# 나의 풀이
from sys import stdin
from collections import deque
def bfs(queue):
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    days = -1
    while queue:
        days += 1
        for _ in range(len(queue)):
            a, b, c = queue.popleft()
            for i in range(6):
                x = a + dx[i]
                y = b + dy[i]
                z = c + dz[i]
                if 0 <= x < N and 0 <= y < M and 0 <= z < H and matrix[z][x][y]==0:
                    matrix[z][x][y] = matrix[c][a][b]+1
                    queue.append([x, y, z])

    for i in matrix:
        for j in i:
            if 0 in j:
                return -1
    return days

def solution():
    queue = deque()
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if matrix[z][x][y] == 1:
                    queue.append([x, y, z])
    return bfs(queue)

M, N, H = map(int, stdin.readline().split())
matrix = [[] for i in range(H)]
for h in range(H):
    for _ in range(N):
        matrix[h].append(list(map(int, list(stdin.readline().split()))))
print(solution())