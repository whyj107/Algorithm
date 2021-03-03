# Grasshopper - Terminal game move function
# https://www.codewars.com/kata/563a631f7cbbc236cf0000c2/train/python

# 나의 풀이
def move(position, roll):
    return position + roll*2

print(move(0, 4), 8)
print(move(3, 6), 15)
print(move(2, 5), 12)