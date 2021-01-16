# Return the first M multiples of N
# https://www.codewars.com/kata/593c9175933500f33400003e/train/python

# 나의 풀이
def multiples(m, n):
    return [n*i for i in range(1, m+1)]

print(multiples(3, 5), [5, 10, 15])