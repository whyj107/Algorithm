# 문제
# 바이러스
# https://www.acmicpc.net/problem/2606

# 나의 풀이
import sys
computer_N = int(sys.stdin.readline())
m = int(sys.stdin.readline())
matrix = [[0]*(computer_N+1) for _ in range(computer_N+1)]
for _ in range(m):
    line = list(map(int, sys.stdin.readline().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1

# 깊이 우선 탐색
def dfs(start, visited):
    visited += [start]
    for c in range(len(matrix[start])):
        if matrix[start][c] == 1 and (c not in visited):
            dfs(c, visited)
    return visited

# 너비 우선 탐색
def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        n = queue.pop(0)
        for c in range(len(matrix[start])):
            if matrix[n][c] == 1 and (c not in visited):
                visited.append(c)
                queue.append(c)
    return visited

print(len(dfs(1, []))-1)
print(len(bfs(1))-1)