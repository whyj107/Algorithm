# Highest and Lowest
# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

# 나의 풀이
def high_and_low(numbers):
    max_n, min_n = max(list(map(int, numbers.split(' ')))), min(list(map(int, numbers.split(' '))))
    return ' '.join([str(max_n), str(min_n)])

# 다른 사람의 풀이
def high_and_low1(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")
print(high_and_low("1 -1"), "1 -1")
print(high_and_low("1 1"), "1 1")
print(high_and_low("-1 -1"), "-1 -1")
print(high_and_low("1 -1 0"), "1 -1")
print(high_and_low("1 1 0"), "1 0")
print(high_and_low("-1 -1 0"), "0 -1")
print(high_and_low("42"), "42 42")