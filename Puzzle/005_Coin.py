# 환전할 때 안 쓰이는 동전은 있어도 되지만, 너무 많은 잔돈이 나오면 곤란하기 때문에
# 각 동전마다 최대 15개까지 환전할 수 있습니다.
# 1,000원 지폐를 넣었을 때 나오는 동전의 조합이 몇 가지인지 구해보세요.
# 동전의 순서는 무시하기로 합니다.

cnt = 0

# 500원 동전은 최대 2개
for coin_500 in range(0, 2+1):
    # 100원 동전은 최대 10개
    for coin_100 in range(0, 10+1):
        # 50원 동전은 최대 15개
        for coin_50 in range(0, 15+1):
            # 10원 동전은 최대 15개
            for coin_10 in range(0, 15+1):
                if coin_500 + coin_100 + coin_50 + coin_10 <= 15:
                    if coin_500*500 + coin_100*100 + coin_50*50 + coin_10*10 == 1000:
                        cnt += 1

print(cnt)

#---------------------------------------------
# deque
# 파이썬에서  shift 함수를 사용하고자 할 때 활용하면 좋은 클래스
from collections import deque

cnt = 0
def change(target, coins, usable):
    global cnt
    coin = coins.popleft()
    if len(coins) == 0:
        if target // coin <= usable:
            cnt += 1
    else:
        for i in range(0, target // coin + 1):
            change(target - coin * i, coins.copy(), usable - i)

change(1000, deque([500, 100, 50, 10]), 15)
print(cnt)
