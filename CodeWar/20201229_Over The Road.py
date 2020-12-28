# Over The Road
# https://www.codewars.com/kata/5f0ed36164f2bc00283aed07/train/python

# 나의 풀이
def over_the_road(address, n):
    return 2*n - address + 1

# 다른 사람의 풀이
def over_the_road1(a, n):
    return 2*n + 1 - a

print(over_the_road(1, 3), 6)
print(over_the_road(3, 3), 4)
print(over_the_road(2, 3), 5)
print(over_the_road(3, 5), 8)
print(over_the_road(7, 11), 16)
print(over_the_road(23633656673, 310027696726), 596421736780)