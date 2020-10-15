# 피보나치 수3
# https://www.acmicpc.net/problem/2749

# 나의 풀이
from sys import stdin
n = int(stdin.readline())

# 메모리 초과
f = [0 for i in range(n+1)]
def fibo1(a):
    f[1] = 1
    if a == 0 or a == 1:
        return a
    for i in range(2, a+1):
        f[i] = (f[i-1] + f[i-2]) % 1000000

# fibo1(n)
# print(f[-1])

# 시간 초과
def fibo2(a, b, c):
    while c != 0:
        tmp = a % 1000000
        a = b % 1000000
        b += tmp
        c -= 1
    return a
# print(fibo1(0, 1, n))

def fibo3(n):
    n1, n2 = 0, 1
    for _ in range(n):
        n1, n2 = n2 % 1000000, (n1+n2) % 1000000
    return n1
# 피사노 주기 : 피보나치 수를 나눈 수는 항상 주기를 가진다.
#             피사노 주기는 15*(10**5)이다.
print(fibo3(n % (15 * (10 ** 5))))