# Guess the Sequence
# https://www.codewars.com/kata/5b45e4b3f41dd36bf9000090/train/python

# 나의 풀이
def sequence(x):
    return list(map(int, sorted([str(i) for i in range(1, x+1)])))

# 다른 사람의 풀이
def sequence1(x):
    return sorted(range(1, x+1), key=str)



print(sequence(16), [1, 10, 11, 12, 13, 14, 15, 16, 2, 3, 4, 5, 6, 7, 8, 9])
print(sequence(9), [1, 2, 3, 4, 5, 6, 7, 8, 9])
