import sys

def dfs(remain, result=[]):
    # dfs에 들어온 함수는 remain으로 들어옴
    # result는
    # M개를 고른 수열 출력
    if len(result) == M:
        for i in result:
            print(i, end=' ')
        # 개행
        print()
        return

    # dfs 핵심
    for idx in range(len(remain)):
        # remain[len(remain)] 일 경우 추가되는 값은 없음
        r = remain[idx]
        remain.remove(r)
        result.append(r)

        dfs(remain, result)
        remain.append(r)
        remain.sort()
        result.pop(-1)

if __name__=='__main__':
    global N, M
    # 입력 받기
    N, M = map(int, sys.stdin.readline().split())
    # 1부터 N까지의 범위로 리스트 생성해서 dfs 함수로 넘긴다.
    # N이 3이면 [1, 2, 3]
    dfs(list(range(1, N+1)))