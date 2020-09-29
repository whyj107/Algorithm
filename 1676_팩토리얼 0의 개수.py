# 문제
# 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676

# 나의 풀이
from sys import stdin
n = int(stdin.readline())
fac = 1
for i in range(1, n+1):
    fac *= i
cnt = 0
while True:
    if fac % 10 == 0:
        cnt += 1
        fac //= 10
    else:
        break
print(cnt)