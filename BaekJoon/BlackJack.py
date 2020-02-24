# N과 M 입력 받기
N, M = map(int, input().split(' '))

# 입력받은 숫자 n이라는 list에 넣기
n = list(map(int, input().split(' ')))
# 답 초기화
answer = 0

# for문을 이용해서 차례대로 더한 다음 값을 구한다.
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if (n[i] + n[j] + n[k]) <= M and (M - (n[i] + n[j] + n[k]) < (M - answer)):
                answer = n[i] + n[j] + n[k]

print(answer)