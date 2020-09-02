# 문제
# 단지번호붙이기
# https://www.acmicpc.net/problem/2667

# 나의 풀이
from sys import stdin
#좌/우/위/아래
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
cnt = []
def bfs(i, j):
    queue = [[i, j]]
    matrix[i][j] = 0
    cnt_ = 1
    while queue:
        a, b = map(int, queue.pop(0))
        for k in range(4):
            x = a+dx[k]
            y = b+dy[k]
            if 0 <= x < n and 0 <= y < n and matrix[x][y] == 1:
                matrix[x][y] = 0
                queue.append([x, y])
                cnt_ += 1
    cnt.append(cnt_)

# 입력 받기 시작
n = int(stdin.readline())
matrix = []
for i in range(n):
    matrix.append(list(map(int, stdin.readline().rstrip())))

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            bfs(i, j)

# 답
print(len(cnt))
for i in sorted(cnt):
    print(i)
