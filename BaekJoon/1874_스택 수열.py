# 문제
# 스택 수열
# https://www.acmicpc.net/problem/1874

# 풀이
from sys import stdin
n = int(stdin.readline())
tmp = [int(stdin.readline()) for i in range(n)]

def numeric():
    cnt, stack, result = 1, [], []
    for i in tmp:
        while cnt <= i:
            stack.append(cnt)
            result.append('+')
            cnt += 1
        if stack.pop() != i:
            return 'NO'
        else:
            result.append('-')
    return '\n'.join(result)

print(numeric())