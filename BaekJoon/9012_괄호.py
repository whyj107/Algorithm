# 문제
# 괄호
# https://www.acmicpc.net/problem/9012

# 나의 풀이
import sys
for i in range(int(sys.stdin.readline())):
    answer = []
    tmp = sys.stdin.readline().rstrip()
    for j in tmp:
        if j == '(':
            answer.append(j)
        elif j == ')':
            if answer != []:
                answer.pop()
            else:
                answer = [1]
                break
    if answer == []:
        print("YES")
    else:
        print("NO")