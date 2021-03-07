# The Feast of Many Beasts
# https://www.codewars.com/kata/5aa736a455f906981800360d/train/python

# 나의 풀이
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]

print(feast("great blue heron", "garlic naan"), True)
print(feast("chickadee", "chocolate cake"), True)
print(feast("brown bear", "bear claw"), False)