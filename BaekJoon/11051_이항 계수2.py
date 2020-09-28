# 문제
# 이항 계수2
# https://www.acmicpc.net/problem/11051

# 나의 풀이
from sys import stdin
n1, n2 = map(int, stdin.readline().split(' '))
answer = 1
for i in range(n1, n1-n2, -1):
    answer *= i
for i in range(1, n2+1):
    answer //= i
print(answer % 10007)