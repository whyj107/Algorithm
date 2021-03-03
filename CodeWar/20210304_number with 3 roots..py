# number with 3 roots.
# https://www.codewars.com/kata/5932c94f6aa4d1d786000028/train/python

# 나의 풀이
def perfect_roots(n):
    return n**0.5 == int(n**0.5) and n**0.25 == int(n**0.25) and n**0.125 == int(n**0.125)

# 다른 사람의 풀이
# We just need to check the 8th root:
# n == x**8
# -> n == (x**2)**4
# -> n == (x**4)**2
def perfect_roots1(n):
    return n**(1/8)%1 == 0

def perfect_roots2(n):
    return (n ** 0.125) % 1 == 0

print(perfect_roots(256), True)
print(perfect_roots(1000), False)
print(perfect_roots(6561), True)