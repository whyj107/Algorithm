# Find the middle element
# https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python

# 나의 풀이
def gimme(input_array):
    return input_array.index(sorted(input_array)[len(input_array)//2])

# 다른 사람의 풀이
def gimme1(arr):
    return arr.index(sorted(arr)[1])

print(gimme([2, 3, 1]), 0, 'Finds the index of middle element')
print(gimme([5, 10, 14]), 1, 'Finds the index of middle element')