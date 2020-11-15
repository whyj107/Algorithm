# Sum two arrays
# https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6/train/python

# 나의 풀이
def sum_arrays(array1,array2):
    if array1 == [] or array2 == []: return max(array1, array2)
    n = int(''.join(str(i) for i in array1)) + int(''.join(str(i) for i in array2))
    tmp = abs(n)
    answer = []
    while tmp >= 10:
        answer.append(tmp%10)
        tmp //= 10
    answer.append(-tmp if n < 0 else tmp)
    return answer[::-1]

# 다른 사람의 풀이
def sum_arrays1(array1,array2):
    if not array1: return array2
    if not array2: return array1
    num = sum(map(lambda x: int(''.join(map(str, x))), [array1, array2]))
    lst = list(map(int, str(abs(num))))
    if num < 0: lst[0] *=-1
    return lst

"""
print(sum_arrays([3,2,9],[1,2]),[3,4,1])
print(sum_arrays([4,7,3],[1,2,3]),[5,9,6])
print(sum_arrays([1],[5,7,6]),[5,7,7])
print(sum_arrays([-3,4,2], [3,4,4]),[2])
print(sum_arrays([-2], [0]), [-2])
print(sum_arrays([0],[]),[0])
print(sum_arrays([],[1,2]),[1,2])
"""
print(sum_arrays([3, 2, 6, 6], [-7, 2, 2, 8]))