# 문제
# 패션왕 신해빈
# https://www.acmicpc.net/problem/9375

# 나의 풀이
# car:[a, b], key:[d]
# len(car) == 2 len(key) == 1
# (2+1)*(1+1) - 1(아무것도 아닐 때)
from sys import stdin
for _ in range(int(stdin.readline())):
    d = dict()
    n = int(stdin.readline())
    for i in range(n):
        a, b = stdin.readline().rstrip().split(' ')
        if b not in d: d[b] = [a]
        else: d[b].append(a)
    answer = 1
    for k in d.keys():
        answer *= len(d[k])+1
    print(answer-1)