# Floating point comparison
# https://www.codewars.com/kata/5f9f43328a6bff002fa29eb8/train/python

# 나의 풀이
def approx_equals(a, b):
    return abs(a-b) < 0.001

# 다른 사람의 풀이
def approx_equals1(a, b):
    return abs(a - b) < 1e-3

def feq(a, b):
    if abs(a-b) < 0.001:
        return 1
    return 0

def approx_equals2(a, b):
    return feq(a, b)

data = (
        (175.9827, 82.25, False),
        (-156.24037, -156.24038, True),
        (123.2345, 123.234501, True),
        (1456.3652, 1456.3641, False),
        (-1.234, -1.233999, True),
        (98.7655, 98.7654999, True),
        (-7.28495, -7.28596, False))

for (a, b, eq) in data:
    print(approx_equals(a, b), eq)