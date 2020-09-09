import sys

N, M = map(int, input().split(' '))

# rstrip : 문자열 오른쪽 제거. chars지정이 없으면 공백문자를 제거.
#          지정이 되어 있으면 chars의 모든 조합을 제거
#          strip과 lstrip도 있다.
B = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

def block_cnt(i, j):
    cntWB, cntBW = 0, 0

    # 각 칸마다 무슨 색인지 cntWB와 cntBW에 기록
    # 8x8 중에서 짝수와 홀수로 나누어서 cntWB와 cntBW로 구분하여 저장 후 값 return
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

# 문제에서 잘라서 8x8칸을 만들기 때문에 N-7과 M-7로 구성
# 1)                        2)                          3)
# oxoxoxox|ox               o|xoxoxoxo|x                ox|oxoxoxox
# xoxoxoxo|xo               x|oxoxoxox|o                xo|xoxoxoxo
# oxoxoxox|ox               o|xoxoxoxo|x                ox|oxoxoxox
# xoxoxoxo|xo               x|oxoxoxox|o                xo|xoxoxoxo
# oxoxoxox|ox               o|xoxoxoxo|x                ox|oxoxoxox
# xoxoxoxo|xo               x|oxoxoxox|o                xo|xoxoxoxo
# oxoxoxox|ox               o|xoxoxoxo|x                ox|oxoxoxox
# xoxoxoxo|xo               x|oxoxoxox|o                xo|xoxoxoxo
# 최소로 고칠 값을 찾기
for i in range(N-7):
    for j in range(M-7):
        cnt1, cnt2 = block_cnt(i, j)
        mini = min(mini, cnt1, cnt2)
print(mini)