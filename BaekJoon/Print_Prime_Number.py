M, N = map(int, input().split())
decimal_list = []

for i in range(M, N+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
            if count > 2:
                break
    if count == 2:
        decimal_list.append(i)

for j in decimal_list:
    print(j)
# 시간 초과
# ----------------------------------------
# num에 1~N+1까지 저장
num = [x for x in range(1, N+1)]
# print(num)
# 0번째에 1 넣어서 숫자와 인덱스를 맞춤
num.insert(0, 1)
# print(num)
# 인덱스 2부터 시작.
# 위에서 0에 1을 넣었기 때문에 인덱스 2에 숫자 2가 들어가게 된다.
for i in range(2, N+1):
    # 2의 배수부터 시작한다.
    j = 2
    # i가 N 배수 아래일 경우 배수 위치의 값을 1로 바꾼다.
    while N >= i*j:
        num[i*j] = 1
        j += 1
# M과 N 사이에서 1이 아닌 것들을 출력
for l in num:
    if l != 1 and M <= l and l <= N :
        print(l)