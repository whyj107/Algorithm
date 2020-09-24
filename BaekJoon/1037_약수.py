# 문제
# 약수
# https://www.acmicpc.net/problem/1037

# 나의 풀이
from sys import stdin
N_CNT = int(stdin.readline())
N_tmp = list(map(int, stdin.readline().split(' ')))
N_tmp.sort()
print(N_tmp[0]*N_tmp[-1])