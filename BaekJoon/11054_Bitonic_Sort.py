# 백준 11054 가장 긴 바이토닉 부분 수열

def solve(N, LIS):
    dp = [1] * N
    dp_increase = [1] * N
    dp_decrease = [1] * N
    for i in range(N):
        for j in range(i):
            if LIS[i] > LIS[j]:
                dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)

    for i in range(N-1, -1, -1):
        for j in range(N-1, i, -1):
            if LIS[i] > LIS[j]:
                dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)
        dp[i] = dp_increase[i] + dp_decrease[i]

    return max(dp) - 1

if __name__=='__main__':
    N = int(input())
    LIS = list(map(int, input().split()))
    print(solve(N, LIS))
