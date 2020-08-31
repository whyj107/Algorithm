# 문제
# 큐2
# https://www.acmicpc.net/problem/18258

# 나의 풀이
# 시간 초과가 뜬다.
"""
import sys
answer = []
def push(n):
    answer.append(n)
def pop():
    if len(answer) > 0:
        print(answer[0])
        del answer[0]
    else:
        print(-1)
def size():
    print(len(answer))
def empty():
    print(1 if len(answer)==0 else 0)
def front():
    print(-1 if len(answer)==0 else answer[0])
def back():
    print(-1 if len(answer)==0 else answer[-1])

for i in range(int(sys.stdin.readline())):
    str_input = sys.stdin.readline().split()
    if str_input[0] == "push":
        push(int(str_input[1]))
    if str_input[0] == "pop":
        pop()
    elif str_input[0] == "size":
        size()
    elif str_input[0] == "empty":
        empty()
    elif str_input[0] == "front":
        front()
    elif str_input[0] == "back":
        back()

# 다른 사람 풀이
# 이것도 시간 초과다....
from collections import deque
import sys
if __name__ == "__main__":

    N = int(input())  # 명령의 수
    order = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]

    q = deque()
    count = 0  # 큐에 들어있는 정수의 개수
    # 명령 진행
    for i in range(len(order)):
        if order[i][0] == "push":
            q.append(int(order[i][1]))
            count += 1
        elif order[i][0] == "pop":
            if count == 0:  # 큐에 들어있는 정수가 없는 경우
                print(-1)
            else:
                print(q.popleft())  # pop 결과
                count -= 1
        elif order[i][0] == "size":
            print(count)  # 큐에 들어있는 정수의 개수
        elif order[i][0] == "empty":
            if count == 0:
                print(1)  # 큐가 비어있으면
            else:
                print(0)
        elif order[i][0] == "front":
            if count == 0:
                print(-1)
            else:
                print(q[0])
        elif order[i][0] == "back":
            if count == 0:
                print(-1)
            else:
                print(q[len(q) - 1])
"""
# 다른 사람 풀이
import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque([])
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        q.append(s[1])
    elif s[0] == 'pop':
        if not q: print(-1)
        else: print(q.popleft())
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if not q: print(1)
        else: print(0)
    elif s[0] == 'front':
        if not q: print(-1)
        else: print(q[0])
    elif s[0] == 'back':
        if not q: print(-1)
        else: print(q[-1])