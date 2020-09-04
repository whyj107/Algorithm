# 문제
# 동전 0
# https://www.acmicpc.net/problem/11047

# 나의 풀이
def COIN(coin, K):
    total_coin_cnt = 0
    coin.sort(reverse=True)
    for i in coin:
        coin_n = K // i
        total_coin_cnt += coin_n
        K -= coin_n * i
    return total_coin_cnt

from sys import stdin
N, K = map(int, stdin.readline().split())
coin = []
for i in range(N):
    c = int(stdin.readline())
    if c <= K:
        coin.append(c)
print(COIN(coin, K))