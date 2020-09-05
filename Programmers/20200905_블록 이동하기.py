# 문제
# 블록 이동하기
# https://programmers.co.kr/learn/courses/30/lessons/60063?language=python3

from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
def bfs(robot, board, m, n):
    q = deque([robot])
    c = [robot]
    cnt = 0
    while q:
        qlen = len(q)
        while qlen:
            x = q.popleft()
            if x == [[m-1, n-2], [m-1, n-1]] or x == [[m-2, n-1], [m-1, n-1]]:
                return cnt
            for i in range(4):
                tmp = []
                flag = 0
                for j in range(2):
                    nx, ny = x[j][0] + dx[i], x[j][1] + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny]== 0:
                        tmp.append([nx, ny])
                    else:
                        flag = 1
                        break
                if not flag:
                    if x[0][0] == x[1][0]:
                        if i == 0 or i == 1: turn(q, c, x, i, '|')
                    elif x[0][1] == x[1][1]:
                        if i == 2 or i == 3: turn(q, c, x, i, '-')
                    tmp.sort()
                    if tmp not in c:
                        q.append(tmp)
                        c.append(tmp)
            qlen -= 1
        cnt += 1

def turn(q, c, x, i, mode):
    if mode == '|':
        for j in range(2):
            nx = x[j]
            ny = [x[j][0] + dx[i], x[j][1]]
            tmp = [nx, ny]
            tmp.sort()
            if tmp not in c:
                q.append(tmp)
                c.append(tmp)
    elif mode == '-':
        for j in range(2):
            nx = [x[j][0], x[j][1]+dy[i]]
            ny = x[j]
            tmp = [nx, ny]
            tmp.sort()
            if tmp not in c:
                q.append(tmp)
                c.append(tmp)

def solution(board):
    m, n = len(board), len(board[0])
    robot = [[0, 0], [0, 1]]
    return bfs(robot, board, m, n)

print(solution([[0, 0, 0, 1, 1],
                [0, 0, 0, 1, 0],
                [0, 1, 0, 1, 1],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0]]), 7)