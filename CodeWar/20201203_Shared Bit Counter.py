# Shared Bit Counter
# https://www.codewars.com/kata/58a5aeb893b79949eb0000f1/train/python

# 나의 풀이
def shared_bits(a, b):
    return f"{a & b:b}".count("1") > 1

def shared_bits1(a, b):
    return bin(a & b).count('1') > 1

print(shared_bits(1, 2), False)
print(shared_bits(16, 8), False)
print(shared_bits(1, 1), False)
print(shared_bits(2, 3), False)
print(shared_bits(7, 10), False)
print(shared_bits(43, 77), True)
print(shared_bits(7, 15), True)
print(shared_bits(23, 7), True)