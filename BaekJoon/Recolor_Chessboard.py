# 주말에 다시보기
import sys

N, M = map(int, input().split(' '))
B = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

def block_cnt(i, j):
    cntWB = 0
    cntBW = 0

    for i2 in range(i, i+8):
        for j2 in range(j, j+8):
            if (i2 - i + j2 - j) % 2 == 0:
                if B[i2][j2] == 'B':
                    cntWB += 1
                else:
                    cntBW += 1
            else:
                if B[i2][j2] == 'W':
                    cntWB += 1
                else:
                    cntBW += 1
    return cntWB, cntBW

mini = N*M

for i in range(N-7):
    for j in range(M-7):
        cnt1, cnt2 = block_cnt(i, j)
        mini = min(mini, cnt1, cnt2)
print(mini)