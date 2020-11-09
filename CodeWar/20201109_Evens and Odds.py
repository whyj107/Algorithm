# Evens and Odds
# https://www.codewars.com/kata/583ade15666df5a64e000058/train/python

# 나의 풀이
def evens_and_odds(n):
    return format(n, 'x' if n % 2 else 'b')

# 다른 사람의 풀이
def evens_and_odds1(n):
    return f"{n:x}" if n % 2 else f"{n:b}"

print(evens_and_odds(2), '10')
print(evens_and_odds(13), 'd')
