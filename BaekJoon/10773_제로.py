# 문제
# 제로
# https://www.acmicpc.net/problem/10773

# 나의 풀이
import sys
K = int(sys.stdin.readline())
answer = []
for i in range(K):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        answer.pop()
    else:
        answer.append(tmp)
print(sum(answer))