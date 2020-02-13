import math
import sys

for _ in range(int(input())):
    # 시작점과 끝점 입력 받기
    x, y = map(int, input().split())
    # 거리를 구해서(y-x) -1을 해줌
    # 이 값에서 루트를 씌워 주고 버림
    X = int((y - x - 1) ** 0.5)

    # 거리와 X제곱+X의 값을 비교해서 짝수에 속하는지 홀수에 속하는지 판별
    if y - x > X ** 2 + X:
        print(2 * X + 1)
    else:
        print(2 * X)

# 좀 더 이해하기 쉬운 다른 방법 #
for _ in range(int(sys.stdin.readline())):
    # x, y 값 입력 받기
    x, y = map(int, sys.stdin.readline().split())

    # 거리 구하여 X에 삽입
    X = y - x

    # 거리의 제곱근을 올림하여 factor에 저장
    factor = math.ceil(math.sqrt(X))

    down = (factor - 1) ** 2
    up = factor ** 2

    # down - 홀수 끝
    # (down+up)/2 - 짝수 끝
    # up - 홀수 끝
    if X >= (down + up) / 2:
        answer = 2 * factor - 1
    else:
        answer = 2 * factor - 2

    print(answer)