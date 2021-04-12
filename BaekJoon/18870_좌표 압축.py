# 좌표 압축
# https://www.acmicpc.net/problem/18870

from sys import stdin

N = int(stdin.readline())
x = list(map(int, stdin.readline().split()))

# 시간 초과
"""
tmp = sorted(list(set(x)))
result = [tmp.index(i) for i in x]
for i in x:
    print(tmp.index(i), end=' ')
"""

# 시간 초과
"""
for i in x:
    cnt = 0
    for j in set(x):
        if i > j:
            cnt += 1
    print(cnt, end=' ')
"""

tmp = list(sorted(set(x)))
# 딕셔너리 사용
tmp = {tmp[i]: i for i in range(len(tmp))}
print(*[tmp[i] for i in x])