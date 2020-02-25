# 입력 받기
N = int(input())
people = []
answer = ""

# 몸무게와 키 입력 받기
for _ in range(N):
    w, h = map(int, input().split(' '))
    people.append((w, h))

# 랭크 매기기
for c in people:
    rank = 1
    for n in people:
        if (c[0] != n[0]) & (c[1] != n[1]):
            if (c[0] < n[0]) & (c[1] < n[1]):
                rank += 1

    answer += str(rank) + " "

# 더 좋은 출력 방법 생각해보기
print(answer)

