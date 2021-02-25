# Descending Order
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

# 나의 풀이
def descending_order(num):
    return int(''.join(sorted([i for i in str(num)], reverse=True)))

# 다른 사람의 풀이


# print(descending_order(0), 0)
print(descending_order(15), 51)
print(descending_order(1201), 2110)