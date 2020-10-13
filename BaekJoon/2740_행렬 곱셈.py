# 문제
# 행렬 곱셈
# https://www.acmicpc.net/problem/2740

# 라이브러리 사용이 안됨....
from sys import stdin
import numpy as np

N, M = map(int, stdin.readline().split(' '))
arr1 = []
for i in range(N):
    arr1.append(list(map(int, stdin.readline().split(' '))))

M, K = map(int, stdin.readline().split(' '))
arr2 = []
for i in range(M):
    arr2.append(list(map(int, stdin.readline().split(' '))))

# np1 = np.array(arr1)
# np2 = np.array(arr2)

# for i in np1.dot(np2):
#     for j in i:
#         print(j, end=' ')

answer = [[0 for _ in range(K)] for _ in range(N)]
for n in range(N):
    for k in range(K):
        for m in range(M):
            answer[n][k] += arr1[n][m] * arr2[m][k]

for i in answer:
    for j in i:
        print(j, end=' ')
    print()