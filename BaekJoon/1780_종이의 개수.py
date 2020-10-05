# 문제
# 종이의 개수
# https://www.acmicpc.net/problem/1780

# 나의 풀이
from sys import stdin
n = int(stdin.readline())
paper = [list(map(int, stdin.readline().split(' '))) for _ in range(n)]
d = {-1: 0, 0: 0, 1: 0}

def div_conq(x, y, n):
    check = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != paper[i][j]:
                # 1
                div_conq(x, y, n//3)
                # 2
                div_conq(x+n//3, y, n//3)
                # 3
                div_conq(x+n*2//3, y, n//3)

                # 4
                div_conq(x, y+n//3, n//3)
                # 5
                div_conq(x+n//3, y+n//3, n//3)
                # 6
                div_conq(x+n*2//3, y+n//3, n//3)

                # 7
                div_conq(x, y+n*2//3, n//3)
                # 8
                div_conq(x+n//3, y+n*2//3, n//3)
                # 9
                div_conq(x+n*2//3, y+n*2//3, n//3)

                return
    d[check] += 1
    return

div_conq(0, 0, n)

for k in d.keys():
    print(d[k])
