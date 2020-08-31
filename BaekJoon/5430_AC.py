# 문제
# AC
# https://www.acmicpc.net/problem/5430

# 풀이
from sys import stdin, stdout
from collections import deque
def AC(p, q):
    p.replace('RR', '')
    q = deque(q)
    tmp = True
    for c in p:
        if c == 'R':
            tmp = False if tmp else True
        elif c == 'D':
            if q and q[0] != '':
                if tmp:
                    q.popleft()
                else:
                    q.pop()
            else:
                return 'error\n'
    return '['+','.join(q)+']\n' if tmp else '['+','.join(reversed(q))+']\n'

T = int(stdin.readline())
for _ in range(T):
    p = stdin.readline()
    n = int(stdin.readline())
    li = stdin.readline().rstrip()[1:-1].split(',')
    if n == 0 : []
    stdout.write(AC(p, li))