# 문제
# 균형잡힌 세상
# https://www.acmicpc.net/problem/4949

# 나의 풀이
import sys
input_str = sys.stdin.readline().rstrip()
while input_str != '.':
    try:
        if input_str[-1] != '.':
            print("no")
        else:
            tmp1 = []
            for i in input_str:
                if i == '(' or i == '[':
                    tmp1.append(i)
                elif i == ')':
                    if tmp1.pop() != '(':
                        tmp1 = [1]
                        break
                elif i == ']':
                    if tmp1.pop() != '[':
                        tmp1 = [1]
                        break
            if tmp1 == []:
                print("yes")
            else:
                print("no")
    except:
        print("no")
    input_str = sys.stdin.readline().rstrip()

# 다른 사람의 풀이
from sys import stdin, stdout

def isvalid(s):
    stack = []
    for c in s:
        if c in '([':
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                return False
        elif c == ']':
            if not stack or stack.pop() != '[':
                return False
    return not stack

strings = stdin.readlines()
strings.pop()
for string in strings:
    stdout.write("yes\n" if isvalid(string) else "no\n")