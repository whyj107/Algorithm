member = []

for _ in range(int(input())):
    age, name = map(str, input().split())
    # 나이는 int로 변형
    age = int(age)
    # (나이, 이름)으로 리스트에 저장
    member.append((age, name))

# 나이(x[0])로 정렬
member.sort(key=lambda x: (x[0]))

for x in member:
    print(x[0], x[1])