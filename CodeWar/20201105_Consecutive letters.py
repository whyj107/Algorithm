# Consecutive letters
# https://www.codewars.com/kata/5ce6728c939bf80029988b57/train/python

# 나의 풀이
def solve(st):
    pre = 0
    for s in sorted([ord(s1) for s1 in st]):
        if pre != 0 and s-pre != 1:
            return False
        pre = s
    return True

# 다른 사람의 풀이
def solve1(s):
    return "".join(sorted(s)) in "abcdefghijklmnopqrstuvwxyz"

print(solve("abc"),True)
print(solve("abd"), False)
print(solve("dabc"),True)
print(solve("abbc"), False)