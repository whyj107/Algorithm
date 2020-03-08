# 콜라츠 추측
# 자연수 n에 대해
# n이 짝수인 경우, n을 2로 나눈다.
# n이 홀수인 경우, n에 3을 곱해 1을 더한다.
# 이 계산을 반복하면 초깃값이 어떤 수였더라도 반드시 1에 도달한다.

# 문제
# 10,000 이하의 짝수 중 앞의 2나 4와 같이 '처음의 수로 돌아가는 수'가 몇 개 있는지 구해 보세요.

# 반복하며 확인
def is_loop(n):
    # 맨 처음에는 3을 곱하고 1을 더함
    check = n * 3 + 1
    # 1이 될 때까지 숫자를 변화시키는 작업 반복
    while check != 1:
        check = check // 2 if check % 2 == 0 else check * 3 + 1
        """
        if check % 2 == 0:
            check = check //2
        else:
            check = check * 3 +1
        """
        if check == n:
            return True
    return False

# 2~10,000 범위의 짝수 확인하기
cnt = 0
for i in range(2, 10000 + 1, 2):
    if is_loop(i):
        cnt += 1
        # print(i, end=" ")
print(cnt, '개')