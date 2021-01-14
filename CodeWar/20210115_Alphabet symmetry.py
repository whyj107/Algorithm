# Alphabet symmetry
# https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/train/python

# 나의 풀이
def solve(arr):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return [sum(1 for index, a2 in enumerate(a1) if index == alpha.find(a2.lower())) for a1 in arr]

# 다른 사람의 풀이
def solve1(arr):
    return [ sum(c == chr(97+i) for i,c in enumerate(w[:26].lower())) for w in arr ]

from operator import eq
from string import ascii_lowercase
def solve2(strings):
    return [sum(map(eq, s.lower(), ascii_lowercase)) for s in strings]

print(solve(["abode","ABc","xyzD"]),[4,3,1])
print(solve(["abide","ABc","xyz"]),[4,3,0])
print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]),[6,5,7])
print(solve(["encode","abc","xyzD","ABmD"]), [1, 3, 1, 3])