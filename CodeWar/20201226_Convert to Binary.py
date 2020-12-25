# Convert to Binary
# https://www.codewars.com/kata/59fca81a5712f9fa4700159a/train/python

# 나의 풀이
def to_binary(n):
    return int(format(n, 'b'))

# 다른 사람의 풀이
def to_binary1(n):
    return int(f'{n:b}')

print(to_binary(1), 1)
print(to_binary(2), 10)
print(to_binary(3), 11)
print(to_binary(5), 101)