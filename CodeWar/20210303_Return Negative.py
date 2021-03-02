# Return Negative
# https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python

# 나의 풀이
def make_negative(n):
    return -n if n > 0 else n

# 다른 사람의 풀이
def make_negative1(number):
    return -abs(number)

print(make_negative(42), -42)
print(make_negative(-9), -9)
print(make_negative(0), 0)