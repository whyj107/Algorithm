# 문제
# 삼각 달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645?language=python3

# 나의 풀이
def solution(n):
    end_num = (n + 1) * n // 2
    answer = [[0] * i for i in range(1, n + 1)]
    offset, num, tmp = 0, 0, 0
    while num < end_num:
        n -= 1

        if offset == n:
            num += 1
            answer[offset][tmp] = num

        for i in range(offset, n):
            num += 1
            answer[i][tmp] = num
        for i in range(offset, n):
            num += 1
            answer[n][i - tmp] = num
        for i in range(offset, n):
            num += 1
            answer[n - i + offset][n - i + tmp] = num
        offset += 2
        tmp += 1
    return sum(answer, [])

print(solution(4))