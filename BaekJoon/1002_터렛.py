# 반복할 횟수 입력 받기
for i in range(int(input())):
    # x1, y1, r1, x2, y2, r2 를 순서대로 입력 받기
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 거리 구하기
    r = ((x1-x2)**2 + (y1-y2)**2)**0.5
    
    if r == 0:
        if r1 == r2:
            answer = -1
        else:
            answer = 0
    else:
        if r < r1+r2:
            if r + min(r1, r2) == max(r1, r2):
                answer = 1
            elif r + min(r1, r2) < max(r1, r2):
                answer = 0
            else:
                answer = 2
        elif r == r1+r2:
            answer = 1
        else:
            answer = 0

    print(answer)
