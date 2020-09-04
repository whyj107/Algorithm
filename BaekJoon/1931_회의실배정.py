# 문제
# 회의실배정
# https://www.acmicpc.net/problem/1931

# 나의 풀이
def solution(time):
    cnt = 1
    end = time[0][1]
    for i in range(1, N):
        if time[i][0] >= end:
            cnt += 1
            end = time[i][1]
    return cnt

from sys import stdin
N = int(stdin.readline())
time = []
for i in range(N):
    s, e = map(int, stdin.readline().split())
    time.append([s, e])
time.sort(key=lambda x: (x[1], x[0]))
print(solution(time))