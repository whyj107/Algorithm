# 파스칼의 삼각형
# 조건 01 : 현재의 숫자는 바로 위의 왼쪽 숫자와 오른쪽 숫자를 덧셈하여 구한다.

N = 12

def combi (n, r):
    p = 1

    for i in range(1, r):
        p = p * (n - i + 1) // i

    return p

if __name__=='__main__':
    for n in range(N + 1):
        t = 0
        while t < (N - n) * 3:
            print(' ', end='')
            t += 1

        for r in range(n + 1):
            print("%3d   " % (combi(n, r)), end='')
        print()