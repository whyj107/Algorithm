# 동적계획법을 사용하여 1부터 N까지의 합 구하기(재귀 호출 사용)
# 조건 01 : f(n) = n + f(n + 1) (1<=n)
# 조건 02 : f(n) = n + f(n + 1) (1<=n)

table = [0 for i in range(200)]
n = 0

def f(k):
    if k == n+1:
        return 0
    table[k] = k + f(k + 1)
    return table[k]

if __name__=='__main__':
    n = 100
    print("%d" % (f(1)))