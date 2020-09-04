# 문제
# ATM
# https://www.acmicpc.net/problem/11399

# 나의 풀이
from sys import stdin
def solution(p):
    p.sort()
    answer = [min(p)]*N
    for i in range(1, len(p)):
        answer[i] = answer[i-1]+p[i]
    return sum(answer)

N = int(stdin.readline())
p = list(map(int, stdin.readline().split()))
print(solution(p))