# 백준
# 스택
# https://www.acmicpc.net/problem/10828

# 나의 풀이
import sys
answer = []
def push(n):
    answer.append(n)
def pop():
    if len(answer)>0:
        print(answer[-1])
        del answer[-1]
    else:
        print(-1)
def size():
    print(len(answer))
def empty():
    print(1 if len(answer)==0 else 0)
def top():
    print(answer[-1] if len(answer) > 0 else -1)

for i in range(int(sys.stdin.readline())):
    str_input = sys.stdin.readline().split()
    if str_input[0] == "push":
        push(int(str_input[1]))
    if str_input[0] == "pop":
        pop()
    elif str_input[0] == "size":
        size()
    elif str_input[0] == "top":
        top()
    elif str_input[0] == "empty":
        empty()