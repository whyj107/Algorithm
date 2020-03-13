import sys

def dfs(remain, result=[]):
    if len(result) == M:
        for i in result:
            print(i, end=' ')
        print()
        return

    # dfs 핵심
    for idx in range(len(remain)):
        result.append(remain[idx])
        dfs(remain, result)
        result.pop(-1)

if __name__=='__main__':
    global N, M
    # 입력 받기
    N, M = map(int, sys.stdin.readline().split())
    dfs(list(range(1, N+1)))