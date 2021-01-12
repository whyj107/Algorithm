# Maximum Multiple
# https://www.codewars.com/kata/5aba780a6a176b029800041c/train/python

# 나의 풀이
def max_multiple(divisor, bound):
    return bound//divisor * divisor

# 다른 사람의 풀이
def max_multiple1(divisor, bound):
    return bound - (bound % divisor)

print(max_multiple(2, 7), 6)
print(max_multiple(3, 10), 9)
print(max_multiple(7, 17), 14)
print(max_multiple(10, 50), 50)
print(max_multiple(37, 200), 185)
print(max_multiple(7, 100), 98)