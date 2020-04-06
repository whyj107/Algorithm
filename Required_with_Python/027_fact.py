# 반복문을 사용하여 팩토리얼 출력하기

# 반복적 방법
def fact1(n):
    fact = 1
    i = n
    while i > 1:
        fact = fact * i
        i = i - 1
    return fact

# 재귀적 방법
def fact2(n):
    if n == 1:
        return 1
    else:
        return n * fact2(n-1)

if __name__=='__main__':
    for i in range(1, 21):
        print("%2d! = %20d" % (i, fact1(i)))
    for i in range(1, 21):
        print("%2d! = %20d" % (i, fact2(i)))