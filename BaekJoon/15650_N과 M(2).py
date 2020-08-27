# N&M(1)과 유사한데 재귀할 때 idx+1을 해줘서 중복을 방지한다.
import sys

def dfs(remain, result=[]):
    if len(result) == M:
        for r in result:
            print(r, end=' ')
        print()
        return

    for idx in range(len(remain)):
        result.append(remain[idx])
        dfs(remain[idx+1:], result)
        result.pop(-1)

if __name__=='__main__':
    global N, M
    N, M = map(int, sys.stdin.readline().split())
    dfs(range(1, N+1))