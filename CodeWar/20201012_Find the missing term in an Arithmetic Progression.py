# 문제
# Find the missing term in an Arithmetic Progression
# https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python

# 나의 풀이
# 시간 초과
def find_missing0(sequence):
    for i in range(sequence[0], sequence[-1], (sequence[-1]-sequence[0])//len(sequence)):
        if i not in sequence:
            return i

def find_missing(sequence):
    tmp = (sequence[-1]-sequence[0])//len(sequence)
    pre = sequence[0]
    for i in range(1, len(sequence)):
        if sequence[i] - pre != tmp:
            return pre+tmp
        pre = sequence[i]

# 다른 사람의 풀이
def find_missing(sequence):
    t = sequence
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)

print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]), 5)
print(find_missing([1, 3, 4, 5, 6, 7, 8, 9]), 2)
