# 문제
# 곱셈
# https://www.acmicpc.net/problem/1629

# 나의 풀이 : 시간 초과
from sys import stdin
a, b, c = map(int, stdin.readline().split(' '))
# print(pow(a, b) % c)

# 나의 풀이
def div_conq(a, b, c):
    if b == 0:
        return 1

    n = div_conq(a, b//2, c)
    result = n * n % c

    if b % 2 == 0:
        return result
    else:
        return a * result % c
print(div_conq(a, b, c))