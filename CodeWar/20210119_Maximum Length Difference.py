# Maximum Length Difference
# https://www.codewars.com/kata/5663f5305102699bad000056/train/python

# 나의 풀이
def mxdiflg(a1, a2):
    if a1 == [] or a2 == []:
        return -1
    ar1_max, ar2_max = len(max(a1, key=len)), len(max(a2, key=len))
    ar1_min, ar2_min = len(min(a1, key=len)), len(min(a2, key=len))
    return ar1_max - ar2_min if ar1_max - ar2_min > ar2_max - ar1_min else ar2_max - ar1_min

# 다른 사람의 풀이
def mxdiflg1(a1, a2):
    if a1 and a2:
        return max(
            len(max(a1, key=len)) - len(min(a2, key=len)),
            len(max(a2, key=len)) - len(min(a1, key=len)))
    return -1

s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2), 13)