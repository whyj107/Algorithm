# Sums of Parts
# https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python

# 나의 풀이
def parts_sums(ls):
    answer = [sum(ls)]
    for i in ls:
        answer.append(answer[-1]-i)
    return answer

# 다른 사람의 풀이
from itertools import accumulate
def parts_sums1(ls):
    return [0, *accumulate(reversed(ls))][::-1]

print(parts_sums([0, 1, 3, 6, 10]), [20, 20, 19, 16, 10, 0])