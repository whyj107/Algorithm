# 문제
# 행렬 제곱
# https://www.acmicpc.net/problem/10830

# 나의 풀이
from sys import stdin

# 시간 초과
"""
def solve(N, A, B):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for n in range(N):
        for k in range(N):
            for m in range(N):
                result[n][k] += (A[n][m] * B[m][k])
            result[n][k] %= 1000
    return result

N, B = map(int, stdin.readline().split(' '))

A = [list(map(int, stdin.readline().split(' '))) for _ in range(N)]

answer = A.copy()

for i in range(B-1):
    answer = solve(N, answer, A)

"""
N, B = map(int, stdin.readline().split(' '))

A = [list(map(int, stdin.readline().split(' '))) for _ in range(N)]

def solve(A, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    elif B % 2 > 0:
        tmp = [[0 for _ in range(N)] for _ in range(N)]
        c = solve(A, B-1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j] += c[i][k] * A[k][j]
                tmp[i][j] %= 1000
        return tmp
    else:
        tmp = [[0 for _ in range(N)] for _ in range(N)]
        c = solve(A, B//2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j] += c[i][k] * c[k][j]
                tmp[i][j] %= 1000
        return tmp

for r in solve(A, B):
    for i in r:
        print(i, end=' ')
    print()