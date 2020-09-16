# 문제
# Will the present fit?
# https://www.codewars.com/kata/52b23340c65ea422b1000045/train/python

# 나의 풀이
def will_fit(present, box):
    for i in zip(sorted(present), sorted(box)):
        if i[0] >= i[1]-1: return False
    return True

# 다른 사람의 풀이
def will_fit1(present: tuple, box: tuple)->bool:
    return all([a-1 > b for a, b in zip(sorted(box), sorted(present))])

print(will_fit((10, 2, 4), (6, 4, 12)), True)
print(will_fit((1, 2, 3), (2, 1, 3)), False)
print(will_fit((39, 5, 8), (60, 15, 6)), False)