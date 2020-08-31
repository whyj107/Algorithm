# 문제
# 연속합
# https://www.acmicpc.net/problem/1912

# 시간 초과
def solve0(n, lst):
    max_sum = -1000
    for i in range(n):
        tmp = 0
        for j in range(i, len(lst)):
            tmp += lst[j]
            max_sum = max(max_sum, tmp)
        if max_sum == sum(lst):
            break
    return max_sum

# O(n)
def solve(n, lst):
    tmp = [0 for _ in range(n)]
    max_sum = -1000
    for i in range(n):
        tmp[i] = max(tmp[i-1] + lst[i], lst[i])
        max_sum = max(max_sum, tmp[i])
    return max_sum

n = int(input())
lst = list(map(int, input().split(' ')))
print(solve(n, lst))