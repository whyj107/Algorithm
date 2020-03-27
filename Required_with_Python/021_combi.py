# 최적화한 조합
# 조건 01 : f(n,r)=f(n,r-1)x(n-r+1)/r 형태로 재귀 호출 형태의 조합 함수를 작성한다.

def combi(n, r):
    if r == n:
        return 1
    elif r == 1:
        return n
    else:
        return combi(n, r - 1) * (n - r + 1) // r

if __name__=='__main__':
    n = 1

    while n <= 5:
        r = 1
        while r <= n:
            print("{0}C{1}={2}".format(n, r, combi(n, r)))
            r = r + 1
        n = n + 1