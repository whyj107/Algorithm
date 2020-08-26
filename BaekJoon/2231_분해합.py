# 입력 받기
n = int(input())
# 답 초기화
answer = 0

# 숫자 0은 의미가 없으므로 1부터 시작
# 1부터 증가하면서 입력 받은 n과 (i + i의 자릿수)이 같을 때 출력
# 같지 않을 경우(== i가 n일 경우) 0 출력
for i in range(1, n+1):
    n_list = list(map(int, str(i)))
    answer = i + sum(n_list)

    if answer == n:
        print(i)
        break

    if i == n:
        print(0)