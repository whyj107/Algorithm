# 에라토스테네스의 체 사용
M = int(input())
N = int(input())

# 범위를 지정
num = list(range(M, N+1))

for i in range(2, N+1):
    for j in num:
        # 자기 자신으로 나뉘는 것은 제외
        if j/i == 1:
            pass
        # 나누어 지는 수 존재 시 삭제
        elif j%i == 0:
            num.remove(j)
        elif j == 1:
            num.remove(j)

if len(num) == 0:
    print(-1)
else:
    print(num)
    # 합 출력
    print(sum(num))
    # 최소값 출력
    print(min(num))
# 틀렸다. 왜지...?
# ----------------------------------
# 맞았다.
decimal_list = []

for i in range(M, N+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
            # count 값이 2 초과하면 소수가 아니다.
            if count > 2:
                break
    if count == 2:
        decimal_list.append(i)
if len(decimal_list) != 0:
    print(decimal_list)
    print(sum(decimal_list))
    print(min(decimal_list))
else:
    print(-1)