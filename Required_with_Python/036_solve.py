# 만들 수 있는 삼각형의 개수 구하기(재귀 호출)
# 조건 01 : 전체 탐색을 위해 삼각형의 세변 a, b, c를 1부터 n까지 증가시키는 반복문을 사용한다.
# 조건 02 : 삼각형이 되는 조건 : a <= b && b <= c && a + b > c을 만족해야 한다.

cnt = 0
checked = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]

def solve(n, a, b, c):
    global cnt

    if a + b + c == n:
        if (a <= b) and (b <= c) and (a+b > c) and (checked[a][b][c] == 0):
            cnt += 1
            checked[a][b][c] = 1
        return

    solve(n, a+1, b, c)
    solve(n, a, b+1, c)
    solve(n, a, b, c+1)

if __name__=='__main__':
    n = 10
    solve(n, 1, 1, 1)
    print("만들 수 있는 삼각형의 갯수: %d" % (cnt))