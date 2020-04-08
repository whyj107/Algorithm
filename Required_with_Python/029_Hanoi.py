# 하노이의 탑
# 조건 01 : 한번에 하나의 원판만 옮길 수 있다.
# 조건 02 : 큰 원판이 작은 원판 위에 있어서는 안된다.

def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print('%d번 원반을 %c에서 %c로 옮김' % (n, a, b))
        hanoi(n-1, c, b, a)

if __name__=='__main__':
    n = int(input('원반의 갯수 : '))
    hanoi(n, 'a', 'b', 'c')