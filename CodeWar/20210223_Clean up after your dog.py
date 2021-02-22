# Clean up after your dog
# https://www.codewars.com/kata/57faa6ff9610ce181b000028/train/python

# 나의 풀이
def crap(garden, bags, cap):
    cnt = 0
    for i in garden:
        cnt += i.count('@')
        if i.count('D') != 0:
            return 'Dog!!'
    return 'Cr@p' if cnt > bags*cap else 'Clean'

# 다른 사람의 풀이
from collections import Counter
from itertools import chain

def crap1(garden, bags, cap):
    c = Counter(chain(*garden))
    return 'Dog!!' if c['D'] else ('Clean','Cr@p')[c['@'] > bags*cap]

print(crap([['_', '_', '_', '_'],
            ['_', '_', '_', '@'],
            ['_', '_', '@', '_']],
           2, 2), "Clean")
print(crap([['_', '_', '_', '_'],
            ['_', '_', '_', '@'],
            ['_', '_', '@', '_']],
           1, 1), "Cr@p")
print(crap([['_', '_'],
            ['_', '@'],
            ['D', '_']],
           2, 2), "Dog!!")
print(crap([['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_']], 2, 2), "Clean")
print(crap([['@', '@'],
            ['@', '@'],
            ['@', '@']], 3, 2), "Clean")