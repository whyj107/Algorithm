# Lost number in number sequence
# https://www.codewars.com/kata/595aa94353e43a8746000120/train/python

# 나의 풀이
def find_deleted_number(arr, mixed_arr):
    return 0 if set(arr) == set(mixed_arr) else list(set(arr)-set(mixed_arr))[0]

# 다른 사람의 풀이
def find_deleted_number1(arr, mixed_arr):
    return sum(arr)-sum(mixed_arr)

print(find_deleted_number([1,2,3,4,5], [3,4,1,5]), 2)
print(find_deleted_number([1,2,3,4,5,6,7,8,9], [1,9,7,4,6,2,3,8]), 5)
print(find_deleted_number([1,2,3,4,5,6,7,8,9], [5,7,6,9,4,8,1,2,3]), 0)