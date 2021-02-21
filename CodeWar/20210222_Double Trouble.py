# Double Trouble
# https://www.codewars.com/kata/57f7796697d62fc93d0001b8/train/python

# 나의 풀이
def trouble(x, t):
    answer = [x[0]]
    for i in range(1, len(x)):
        if answer[-1] + x[i] == t:
            continue
        answer.append(x[i])
    return answer

TESTS = [
    [([1, 3, 5, 6, 7, 4, 3], 7), [1, 3, 5, 6, 7, 4]],
    [([4, 1, 1, 1, 4],2), [4, 1, 4]],
    [([2, 6, 2], 8), [2, 2]],
    [([2, 2, 2, 2, 2, 2], 4), [2]],
]

for inp, exp in TESTS:
    print(trouble(*inp), exp)