# 오큰수
# https://www.acmicpc.net/problem/17298

# 어렵다 어려워....
# 어렵기도 한데 문제 좀 잘 읽고 출력물 확인하자...
from sys import stdin
def solve(n, l):
    answer = [-1] * n
    idx, stack_tmp = 0, [0]
    while stack_tmp and idx < n:
        while stack_tmp and l[stack_tmp[-1]] < l[idx]:
            answer[stack_tmp.pop()] = l[idx]
        stack_tmp.append(idx)
        idx += 1
    return answer
n = int(stdin.readline())
input_list = list(map(int, stdin.readline().split()))
for i in solve(n, input_list):
    print(i, end=" ")