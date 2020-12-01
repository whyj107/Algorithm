# Will there be enough space?
# https://www.codewars.com/kata/5875b200d520904a04000003/train/python

# 나의 풀이
def enough(cap, on, wait):
    return abs(on+wait-cap) if on+wait > cap else 0

# 다른 사람의 풀이
def enough1(cap, on, wait):
    return max(0, wait - (cap - on))

print(enough(10, 5, 5), 0)
print(enough(100, 60, 50), 10)
print(enough(20, 5, 5), 0)