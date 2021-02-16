# Stringy Strings
# https://www.codewars.com/kata/563b74ddd19a3ad462000054/train/python

# 나의 풀이
def stringy(size):
    return ("10"*(size//2+1))[:size]

# 다른 사람의 풀이
def stringy1(size):
    return "10" * (size / 2) + "1" * (size % 2)

print(stringy(10)[0], '1')
print(stringy(3), '101')
print(stringy(5), '10101')
print(stringy(12), '101010101010')
print(stringy(26), '10101010101010101010101010')
print(stringy(28), '1010101010101010101010101010')