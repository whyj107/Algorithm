N, M = map(int, input().split())
visited = [False]*N
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solve(depth + 1, N, M)
            visited[i] = False
            out.pop()

solve(0, N, M)
# -------------------------------------
from itertools import permutations
N, M = map(int, input().split())
P = permutations(range(1, N+1), M)  # iter(tuple)
for i in P:
    print(' '.join(map(str, i)))
# -------------------------------------
import sys
def testCase():
    input_val = list(map(int, sys.stdin.readline().split()))
    global N, M
    N, M = input_val

def dfs(remain, result = []):
    if len(result) == M:
        for i in result:
            print(i, end=' ')
        print()
        return

    for r in remain:
        remain.remove(r)
        result.append(r)

        dfs(remain, result)

        remain.append(r)
        remain.sort()
        result.pop(-1)

if __name__=='__main__':
    testCase()
    dfs(list(range(1, N+1)))
# -------------------------------------
import itertools
def testCase():
    val = list(map(int, sys.stdin.readline().split()))
    global N, M
    N, M = val

def solve(remain):
    res = list(map(' '.join, itertools.permutations(remain, M)))
    print('\n'.join(res))

if __name__=='__main__':
    testCase()
    solve(map(str, list(range(1, N+1))))