# 동적계획법을 사용하여 피보나치 수 구하기
# 조건 01 : fn = fn-1 + fn-2 (n > 2)
# 조건 02 : fn = fn-1 + fn-2 (n > 2)

table = [0 for i in range(100)]
def fib(n):
    if n==0 or n==1:
        return n
    table[0] = 0
    table[1] = 1

    for i in range(2, n+1):
        table[i] = table[i - 1] + table[i - 2]

if __name__=='__main__':
    fib(30)
    for i in range(31):
        print("피보나치 %2d=%10d" % (i, table[i]))