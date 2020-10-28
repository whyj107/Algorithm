# Reverser
# https://www.codewars.com/kata/58069e4cf3c13ef3a6000168/train/python

# 나의 풀이
def reverse(n):
    return int(''.join([i for i in reversed(str(n))]))

# 다른 사람의 풀이
def reverse1(n):
    m = 0
    while n > 0:
        n, m = n // 10, m * 10 + n % 10
    return m

def reverse2(n):
    return int(str(n)[::-1])

print(reverse(1234), 4321)
print(reverse(10987), 78901)
print(reverse(1020), 201)