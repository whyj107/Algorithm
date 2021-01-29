# Get decimal part of the given number
# https://www.codewars.com/kata/586e4c61aa0428f04e000069/train/python

# 나의 풀이
def get_decimal(n):
    return abs(n) - int(abs(n))

# 다른 사람의 풀이
def get_decimal1(n):
    return abs(n) % 1

print(get_decimal(10), 0)
print(get_decimal(-1.2), 0.2)
print(get_decimal(4.5), 0.5)