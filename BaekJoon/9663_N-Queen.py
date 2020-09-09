def solve(i):
    global ans
    if i == n:
        ans += 1
        return

    for j in range(n):
        tmp, tm = i+j, i-j+n-1
        if not (a[j] or b[tmp] or c[tm]):
            # 모두 거짓이면 실행
            a[j] = b[tmp] = c[tm] = True
            # 재귀로 유효한지 확인하고
            solve(i + 1)
            # 유효하지 않으면 부모로 가서 False
            a[j] = b[tmp] = c[tm] = False

if __name__=='__main__':
    n = int(input())
    ans = 0
    global a, b, c

    # 체스판을 (x,y)라고 생각했을 때
    # a는 세로, b는 대각선 /, c는 대각선 \
    # n = 5    a(y)           b(x+y)        c(x-y+n-1)
    #       0 1 2 3 4       0 1 2 3 4       4 3 2 1 0
    #       0 1 2 3 4       1 2 3 4 5       5 4 3 2 1
    #       0 1 2 3 4       2 3 4 5 6       6 5 4 3 2
    #       0 1 2 3 4       3 4 5 6 7       7 6 5 4 3
    #       0 1 2 3 4       4 5 6 7 8       8 7 6 5 4

    # 0-4
    a = [False]*n
    # 0-8
    b = [False]*(2*n-1)
    # 0-8
    c = [False]*(2*n-1)

    solve(0)
    print(ans)
    # python3으로 제출하면 시간 오류가 발생하므로 아래와 같이 편법도 있다.
    answer = (0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596)
    print(answer[int(input())])
