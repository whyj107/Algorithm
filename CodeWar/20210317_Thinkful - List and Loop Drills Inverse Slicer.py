# Thinkful - List and Loop Drills: Inverse Slicer
# https://www.codewars.com/kata/586ec0b8d098206cce001141/train/python

# 나의 풀이
def inverse_slice(items, a, b):
    return [i for idx, i in enumerate(items) if not a <= idx < b]

# 다른 사람의 풀이
def inverse_slice1(items, a, b):
    return items[:a] + items[b:]

def inverse_slice2(items, a, b):
    del items[a:b]
    return items

print(inverse_slice([12, 14, 63, 72, 55, 24], 2, 4), [12, 14, 55, 24])
print(inverse_slice([12, 14, 63, 72, 55, 24], 0, 3), [72, 55, 24])
print(inverse_slice(['Intuition', 'is', 'a', 'poor', 'guide', 'when', 'facing', 'probabilistic', 'evidence'], 5, 13), ['Intuition', 'is', 'a', 'poor', 'guide'])