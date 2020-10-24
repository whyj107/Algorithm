# Basic Sequence Practice
# https://www.codewars.com/kata/5436f26c4e3d6c40e5000282/train/python

# 나의 풀이
def sum_of_n(n):
    answer = []
    cnt = 0
    for i in range(abs(n)+1):
        cnt += -i if n < 0 else i
        answer.append(cnt)
    return answer

# 다른 사람의 풀이
def sum_of_n1(n):
    sign, n = (1, -1)[n < 0], abs(n)
    return [sign * (i * i + i) / 2 for i in range (n + 1)]

print(sum_of_n(3), [0, 1, 3, 6])
print(sum_of_n(1), [0, 1])
print(sum_of_n(0), [0])
print(sum_of_n(-4), [0, -1, -3, -6, -10])