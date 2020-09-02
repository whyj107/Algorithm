# 문제
# 미로 탐색
# https://www.acmicpc.net/problem/2178

# 나의 풀이
from sys import stdin
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q = [(i, j)]
    check = [[False] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]

    # 시작점
    check[i][j] = True
    dist[i][j] = 1

    while q:
        a, b = q.pop(0)
        for k in range(4):
            x, y = a + dx[k], b + dy[k]
            if 0 <= x < n and 0 <= y < m:
                if check[x][y] == False and matrix[a][b] == 1:
                    q.append((x, y))
                    dist[x][y] = dist[a][b] + 1
                    check[x][y] = True
    return dist[n-1][m-1]

# 입력
n, m = map(int, stdin.readline().rstrip().split())
matrix = [list(map(int, list(stdin.readline().rstrip()))) for _ in range(n)]
# 출력
print(bfs(0, 0))