# 8 towers
# https://www.codewars.com/kata/535bea76cdbf50281a00004c/train/python

# 나의 풀이
# 팩토리얼 문제이다.
def tower_combination(n):
    return 1 if n==0 else n * tower_combination(n-1)

# 다른 사람의 풀이
import math
def tower_combination1(n):
    return math.factorial(n)

# from math import factorial as tower_combination

print(tower_combination(2) == 2)
print(tower_combination(3) == 6)