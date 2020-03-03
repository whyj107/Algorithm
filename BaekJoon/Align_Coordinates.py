# list 생성
dots = []

# 좌표 입력
for _ in range(int(input())):
    dots.append(list(map(int, input().split())))

# key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬
# 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬
# 그리고 그 안에서 다음 두 번째 인자를 기준으로 정렬
# 만약 내림차순으로 정렬하고 싶으면 -x[0] 이런 식으로 사용
dots.sort(key=lambda x: (x[0], x[1]))

# 좌표 출력
for [i, j] in dots:
    print(i, j)

