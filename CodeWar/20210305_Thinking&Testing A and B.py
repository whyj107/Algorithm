# Thinking & Testing: A and B?
# https://www.codewars.com/kata/56d904db9963e9cf5000037d/train/python

# 나의 풀이
# 비트 논리 연산자 사용하여 푸는 문제이다.
# AND : a&b
# OR : a|b
# XOR : a^b
# NOT : ~a
def testit(a, b):
    return a | b

# a + b ?
print(testit(0, 1), 1)
print(testit(1, 2), 3)
print(testit(10, 20), 30)

# a * b ?
print(testit(1, 1), 1)
print(testit(1, 3), 3)