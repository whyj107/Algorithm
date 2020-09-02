# 문제
# 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206

# 풀이
from sys import stdin
input = stdin.readline

def bfs(y, x, wall):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = [[y, x, wall]]
    dist[y][x][wall] = 1
    while q:
        now = q.pop(0)
        for i in range(4):
            y, x, z = now
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < M and 0 <= ny < N:
                if matrix[ny][nx] == 0 and dist[ny][nx][z] == 0:
                    dist[ny][nx][z] = dist[y][x][z] + 1
                    q.append([ny, nx, z])
                if z == 0 and matrix[ny][nx] == 1 and dist[ny][nx][z + 1] == 0:
                    dist[ny][nx][z + 1] = dist[y][x][z] + 1
                    q.append([ny, nx, z + 1])
def solve():
    bfs(0, 0, 0)
    if dist[-1][-1][0] != 0 and dist[-1][-1][1] != 0:
        return min(dist[-1][-1][0], dist[-1][-1][1])
    elif dist[-1][-1][0] != 0:
        return dist[-1][-1][0]
    elif dist[-1][-1][1] != 0:
        return dist[-1][-1][1]
    else:
        return -1

# 입력
N, M = map(int, input().split())
matrix = [[] for i in range(N)]
for i in range(N):
    matrix[i] = list(map(int, input().strip()))
dist = [[[0, 0] for j in range(M)] for i in range(N)]
print(solve())