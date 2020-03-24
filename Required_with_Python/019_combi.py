# 반복문을 사용하여 조합(nCr) 구하기

def combi(n, r):
    i = 1
    p = 1
    while i <= r:
        p = p * (n - i + 1) // i
        i = i + 1
    return p

if __name__=='__main__':
    n = 0

    while n <= 5:
        r = 0
        while r <= n:
            print("{0}C{1} = {2}".format(n, r, combi(n, r)))
            r = r+ 1
        n = n+1