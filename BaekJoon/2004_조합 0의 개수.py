# 문제
# 조합 0의 개수
# https://www.acmicpc.net/problem/2004

# 나의 풀이
def cntNum(n, div):
    cnt = 0
    while n != 0:
        n //= div
        cnt += n
    return cnt

from sys import stdin
n, m = map(int, stdin.readline().split(" "))
print(min(cntNum(n, 2)-cntNum(m, 2)-cntNum(n-m, 2), cntNum(n, 5)-cntNum(m, 5)-cntNum(n-m, 5)))