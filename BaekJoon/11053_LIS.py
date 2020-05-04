# 백준 11053 가장 긴 증가하는 부분 수열

def solve(N, LIS):
    # 동적 계획법 사용을 위한 초기화
    dp = [1] * N
    # N만큼 반복
    for i in range(N):
        # i만큼 반복
        for j in range(i):
            if LIS[i] > LIS[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

if __name__=='__main__':
    N = int(input())
    LIS = list(map(int, input().split()))
    print(solve(N, LIS))