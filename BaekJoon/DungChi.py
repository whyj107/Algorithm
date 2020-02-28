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
        # c 보다 n이 몸무게와 키가 더 크면 덩치가 작은 것 이기 때문에
        # rank를 하나씩 올림
        if (c[0] != n[0]) & (c[1] != n[1]):
            if (c[0] < n[0]) & (c[1] < n[1]):
                rank += 1

    answer += str(rank) + " "

# 더 좋은 출력 방법 생각해보기
print(answer)

