# 문제
# Multiply characters
# https://www.codewars.com/kata/52e9aa89b5acdd26d3000127/train/python

# 나의 풀이
def spam(number):
    return ''.join(['hue' for i in range(number)])

# 다른 사람의 풀이
def spam1(number):
    return 'hue' * number

print(spam(1), "hue", "spam(1) should return 'hue'")
print(spam(6), "huehuehuehuehuehue", "spam(6) should return 'huehuehuehuehuehue'")
print(spam(14), "huehuehuehuehuehuehuehuehuehuehuehuehuehue", "spam(14) should return 'huehuehuehuehuehuehuehuehuehuehuehuehuehue'")