# Stones on the Table
# https://www.codewars.com/kata/5f70e4cce10f9e0001c8995a/train/python

# 나의 풀이
def solution(stones):
    return sum([1 for i in range(len(stones)-1) if stones[i] == stones[i+1]])

# 다른 사람의 풀이
import re
def solution1(stones):
    return sum(len(m[0])-1 for m in re.finditer(r'(.)\1+', stones))

print(solution("RGBRGBRGGB"), 1)
print(solution("RGGRGBBRGRR"), 3)
print(solution("RRRRGGGGBBBB"), 9)
