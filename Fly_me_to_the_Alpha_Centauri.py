for _ in range(int(input())):
    #시작점과 끝점 입력 받기
    x, y = map(int, input().split())
    #거리를 구해서(y-x) -1을 해줌
    # 이 값에서 루트를 씌워 주고 버림
    X = int((y-x-1)**0.5)

    # 거리와 X제곱+X의 값을 비교해서 짝수에 속하는지 홀수에 속하는지 판별
    if y-x > X**2 + X:
        print(2*X+1)
    else:
        print(2*X)
