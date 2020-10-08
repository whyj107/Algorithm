# 문제
# 이항 계수3
# https://www.acmicpc.net/problem/11401

from sys import stdin

"""
페르마
"""

def div_conq(n1, n2):
    if n2 == 0:
        return 1
    elif n2 == 1:
        return n1

    if n2 % 2 != 0:
        return div_conq(n1, n2 - 1) * n1
    else:
        return div_conq(n1, n2 // 2) ** 2 % tmp


N, K = map(int, stdin.readline().split())

n = 1
nk = 1
tmp = 1000000007

for num in range(1, N + 1):
    n *= num
    n %= tmp

for num in range(1, K + 1):
    nk *= num
    nk %= tmp

for num in range(1, N - K + 1):
    nk *= num
    nk %= tmp

nk = div_conq(nk, tmp - 2) % tmp

print((n * nk) % tmp)

"""
유클리드
def euclidean(x, y):
    # Finding a, b such that ax+by = gcd(x,y)
    q = []
    while y:
        q.append(x // y)
        (x, y) = (y, x % y)
    q.pop()

    a, b = 0, 1
    for i in q[-1::-1]:
        a, b = b, a - i*b
    return x, a, b


def main(n, m, mod):
    m = min(m, n-m)
    if m == 0:
        return 1
    top = n
    bot = 1
    n += 1
    for i in range(2,m+1):
        top = top*(n-i)%mod
        bot = bot*i%mod
    g, inv, _ = euclidean(bot, mod)
    return top*inv%mod

mod = 1000000007 #prime
n, m = map(int, input().split())
print(main(n, m, mod))
"""