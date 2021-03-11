# Reverse the bits in an integer
# https://www.codewars.com/kata/5959ec605595565f5c00002b/train/python

# 나의 풀이
def reverse_bits(n):
    return int(format(n, 'b')[::-1], 2)

# 다른 사람의 풀이
def reverse_bits1(n):
    return int(f'{n:b}'[::-1],2)

print(reverse_bits(417), 267)
print(reverse_bits(267), 417)
print(reverse_bits(0), 0)
print(reverse_bits(2017), 1087)
print(reverse_bits(1023), 1023)
print(reverse_bits(1024), 1)