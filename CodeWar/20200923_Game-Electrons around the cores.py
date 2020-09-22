# 문제
# Game - Electrons around the cores
# https://www.codewars.com/kata/52210226578afb73bd0000f1/train/python

# 문제를 이해하는게 더 어려웠던 문제
# 나의 풀이
def electrons_around_the_cores(dice):
  return sum([d - 1 for d in dice if d in [3, 5]])

# 다른 사람의 풀이
electrons = {3: 2, 5: 4}
def electrons_around_the_cores1(dice):
  return sum(electrons.get(d, 0) for d in dice)