# list 생성
dots = []

# 좌표 입력
for _ in range(int(input())):
    dots.append(list(map(int, input().split())))

dots.sort(key=lambda x: (x[1], x[0]))

# 좌표 출력
for [i, j] in dots:
    print(i, j)

