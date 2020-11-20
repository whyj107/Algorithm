# Going to the cinema
# https://www.codewars.com/kata/562f91ff6a8b77dfe900006e/train/python

# 문제를 이해하기 힘들어서 풀이를 보고 문제를 이해했다.

# 다른 사람의 풀이1
from itertools import count
from math import ceil

def movie(card, ticket, perc):
    num, A, B = 0, 0, card
    while ceil(B) >= A:
        num += 1
        A += ticket
        B += ticket * (perc ** num)
    return num

# 다른 사람의 풀이2
def movie1(card, ticket, perc):
    return next( x for x in count(card//ticket)
                 if ticket * x > ceil(card + ticket * perc * (1 - perc**x)/(1 - perc)) )

print(movie(500, 15, 0.9), 43)
print(movie(100, 10, 0.95), 24)