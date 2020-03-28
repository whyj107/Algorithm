# 계단에 서서 수다 떨기

# 문제
# 10단짜리 계단에서 같은 방식으로 이동했을 때 두 사람이 같은 단에 서는 방법은 몇 가지인지 구해보세요.

N = 10
STEPS = 4

def move(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    cnt = 0
    for da in range(1, STEPS + 1):
        for db in range(1, STEPS + 1):
            cnt += move(a + da, b - db)
    return cnt
# A:0 B:N
print(move(0, N))

"""
동적 계획법
"""
dp = [0] * (N + 1)
cnt = 0
dp[N] = 1

for i in range(0, N):
    for j in range(0, N + 1):
        for k in range(1, STEPS + 1):
            if k > j:
                break
            # print(j-k, j)
            dp[j - k] += dp[j]
        dp[j] = 0
    if i % 2 == 1:
        cnt += dp[0]

print(cnt)