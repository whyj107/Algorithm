# 재귀 호출을 사용하여 팩토리얼 출력하기

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

if __name__=='__main__':
    for i in range(21):
        print("%2d!=%20d" % (i, fact(i)))