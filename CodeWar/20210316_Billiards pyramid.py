# Billiards pyramid
# https://www.codewars.com/kata/5bb3e299484fcd5dbb002912/train/python

# 나의 풀이
def pyramid(balls):
    cnt = 0
    while balls >= cnt:
        balls -= cnt
        cnt+=1
    return cnt - 1

# 다른 사람의 풀이
def pyramid1(balls):
    return ((8*balls + 1)**.5 - 1) // 2

print(pyramid(1), 1)
print(pyramid(4), 2)
print(pyramid(20), 5)
print(pyramid(100), 13)
print(pyramid(9999), 140)