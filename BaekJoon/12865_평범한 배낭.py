# 문제
# 평범한 배낭
# https://www.acmicpc.net/problem/12865

def solve0(N, K, lst):
    tmp = [[0]*(K+1) for _ in range(N+1)]
    max_value = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            w, v = lst[i][0], lst[i][1]
            if j < w:
                tmp[i][j] = tmp[i-1][j]
            else:
                tmp[i][j] = max(v+tmp[i-1][j-w], tmp[i-1][j])
            max_value = max(max_value, tmp[i][j])
    return max_value

def solve(N, K, lst):
    tmp = [0 for _ in range(K+1)]
    for i in range(N):
        for j in range(K, 1, -1):
            if lst[i][0] <= j:
                tmp[j] = max(tmp[j], tmp[j-lst[i][0]]+lst[i][1])
    return tmp[-1]

N, K = map(int, input().split(' '))
lst = [list(map(int, input().split(' '))) for i in range(N)]
lst.insert(0, [0, 0])
print(solve(N, K, lst))