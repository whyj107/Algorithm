# 0 0 0 입력 받기 전까지 계속 반복
while True:
    # 입력 받기
    line = list(map(int, input().split()))

    # 0 0 0 입력 받으면 종료
    if line == [0, 0, 0]:
        break
    # 정렬
    line.sort()

    # 피타고라스 정리
    if line[0]**2 + line[1]**2 == line[2]**2:
        print("right")
    else:
        print("wrong")