# 문제
# Least Common Multiple
# Write a function that calculates the least common multiple of its arguments;
# each argument is assumed to be a non-negative integer.
# In the case that there are no arguments
# (or the provided array in compiled languages is empty),
# return 1.

# 입력 == 출력
# test.assert_equals(lcm(2,5),10)
# test.assert_equals(lcm(2,3,4),12)
# test.assert_equals(lcm(9),9)
# test.assert_equals(lcm(0),0)
# test.assert_equals(lcm(0,1),0)

# My Code
def lcm(*args):
    if args == []:
        return 1
    elif len(args) < 2:
        return args[0]
    lcm_t = 1
    for i in args:
        lcm_t = lcm_t * i // gcd(lcm_t, i)
    return lcm_t

def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

# Warriors Code
from functools import reduce
def lcm1(*args):
    return reduce(lcms1, args) if args else 1
def gcd1(a, b):
    """Euclidean Algorithm"""
    return b if a == 0 else gcd1(b % a, a)
def lcms1(a, b):
    return (a * b) // gcd1(a, b)


if __name__ == '__main__':
    print(lcm(2, 5))
    print(lcm(2, 3, 4))
    print(lcm(2, 3, 4, 6, 8))
    print(lcm(0))