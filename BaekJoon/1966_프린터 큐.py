# 문제
# 프린터 큐
# https://www.acmicpc.net/problem/1966

# 나의 풀이
import sys
from collections import deque
def solution(priorities, location):
    answer = 0
    while len(priorities) != 0:
        if location == 0:
            if priorities[0] < max(priorities):
                priorities.append(priorities.popleft())
                location = len(priorities) - 1
            else:
                return answer + 1
        else:
            if priorities[0] < max(priorities):
                priorities.append(priorities.popleft())
                location -= 1
            else:
                priorities.popleft()
                location -= 1
                answer += 1

for i in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    p = deque(list(map(int, sys.stdin.readline().split())))
    print(solution(p, M))