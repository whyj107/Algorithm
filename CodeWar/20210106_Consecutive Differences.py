# Consecutive Differences
# https://www.codewars.com/kata/5ff22b6e833a9300180bb953/train/python

# 나의 풀이
def differences(lst):
    while len(lst) != 1:
        answer = []
        for i in range(len(lst)-1):
            answer.append(abs(lst[i] - lst[i+1]))
        lst = answer.copy()
    return lst[0]

# 다른 사람의 풀이
def differences1(lst):
    lst = lst or [0]
    while len(lst) > 1:
        lst = [abs(x-y) for x,y in zip(lst, lst[1:])]
    return lst[0]

print(differences([1, 2, 3]), 0)
print(differences([1, 5, 2, 7, 8, 9, 0]), 1)
print(differences([2, 3, 1]), 1)
print(differences([-1, 2, 3]), 2)