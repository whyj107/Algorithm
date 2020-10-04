# 문제
# 쿼드트리
# https://www.acmicpc.net/problem/1992

# 풀이
from sys import stdin
n = int(stdin.readline())
v = [list(map(int, stdin.readline().strip())) for _ in range(n)]

def div_conq(x, y, n):
    check = v[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != v[i][j]:
                print('(', end='')

                div_conq(x, y, n//2)
                div_conq(x, y+n//2, n//2)
                div_conq(x+n//2, y, n//2)
                div_conq(x+n//2, y+n//2, n//2)

                print(')', end='')
                return
    print('0' if check == 0 else '1', end='')
    return
div_conq(0, 0, n)