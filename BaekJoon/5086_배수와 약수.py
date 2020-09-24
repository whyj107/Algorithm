# 문제
# 배수와 약수
# https://www.acmicpc.net/problem/5086

# 나의 풀이
from sys import stdin
def solution(n1, n2):
    if n2 % n1 == 0:
        return "factor"
    elif n1 % n2 == 0:
        return "multiple"
    else:
        return "neither"

while True:
    n1, n2 = map(int, stdin.readline().split(' '))
    if n1==0 and n2 == 0:
        break
    print(solution(n1, n2))