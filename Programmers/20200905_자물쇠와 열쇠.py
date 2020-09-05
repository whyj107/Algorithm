# 문제
# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3

# 풀이
def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] += key[i][j]
def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M + i][M + j] != 1: return False
    return True
def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] -= key[i][j]

def solution(key, lock):
    M, N = len(key), len(lock)
    board = [[0] * (M * 2 + N) for _ in range(M * 2 + N)]
    for i in range(N):
        for j in range(N):
            board[M + i][M + j] = lock[i][j]
    rotated_key = key
    for _ in range(4):
        rotated_key = list(zip(*rotated_key[::-1]))
        for x in range(1, M + N):
            for y in range(1, M + N):
                attach(x, y, M, rotated_key, board)
                if check(board, M, N): return True
                detach(x, y, M, rotated_key, board)
    return False

if __name__ == '__main__':
    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
                   [[0, 1], [1, 0]]), True)