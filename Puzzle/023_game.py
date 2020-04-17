# 블랙잭으로 대박!?

# 문제
# 맨 처음 칩을 10개 갖고 있을 때,
# 게임을 24번 하여 수중에 칩이 남을 때의 개수 변화는 몇 가지가 있는지 구해 보세요.

memo = {}

def game(coin, depth):
    key = (coin, depth)
    if key in memo:
        return memo[key]
    if coin == 0:
        return 0
    if depth == 0:
        return 1

    # 이길 때
    win = game(coin + 1, depth - 1)
    # 질 때
    lose = game(coin - 1, depth - 1)

    memo[key] = win + lose
    return memo[key]

print(game(10, 24))