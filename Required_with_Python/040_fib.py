# 재귀 호출을 사용하여 피보나치 수 구하기
# 조건 01 : fn = fn-1 + fn-2 (n > 2)
# 조건 02 : fn = fn-1 + fn-2 (n > 2)

# 하지만 너무 느리다.
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__=='__main__':
    for i in range(41):
        # print('피보나치 %2d = %10d' % (i, fib(i)))
        pass

    fibo = [0 for _ in range(41)]
    fibo[1] = 1
    fibo[2] = 1
    print('피보나치 %2d = %10d' % (1, fibo[1]))
    print('피보나치 %2d = %10d' % (2, fibo[2]))
    for i in range(3, len(fibo)):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
        print('피보나치 %2d = %10d' % (i, fibo[i]))