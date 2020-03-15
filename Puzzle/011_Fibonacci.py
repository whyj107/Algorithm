# 피보나치 수열

# 문제
# 피보나치 수열 중 각 자리의 숫자를 더한 수로 나누어 떨어지는 수를
# 다음의 예에 이어 작은 쪽부터 5개 구해보세요.

# 힌트
# 피보나치 수열은 값이 금방 커지기 때문에 자릿수에 주의합시다.

a = b = 1
count = 0
answer = []

while count < 11:
    c = a + b
    # 1자리씩으로 분할하여 각 자리의 합을 취득
    sum = 0
    for e in str(c):
        sum += int(e)
    if c % sum == 0:
        # 나누어 떨어지면 출력
        answer.append(c)
        count += 1
    a, b = b, c

for i in answer[-5:]:
    print(i)