# 반복문을 사용하여 피보나치 수열 구하기
# 조건 01 : 위의 점화식대로 n이 0이거나 1일 때의 피보나치 수는 1이 된다.
# 조건 02 : 현재의 i에 대한 피보나치 수 fib_i는 이전 피보나치 수인 fib_i_1과 fib_i_2의 합으로 구할 수 있다.

def fib(n):
    a = 1
    b = 1

    for k in range(3, n):
        dummy = b
        b += a
        a = dummy

    return b

if __name__=='__main__':
    for i in range(41):
        print('피보나치 %2d = %10d' % (i, fib(i)))