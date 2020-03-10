# 문제
# You are going to be given an array of integers.
# Your job is to take that array and find an index N
# where the sum of the integers to the left of N is equal to the sum of the integers to the right of N.
# If there is no index that would make this happen, return -1.

# For example:
# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3,
# because at the 3rd position of the array,
# the sum of left side of the index ({1,2,3})
# and the sum of the right side of the index ({3,2,1}) both equal 6.
#
# Let's look at another one.
# You are given the array {1,100,50,-51,1,1}:
# Your function will return the index 1,
# because at the 1st position of the array,
# the sum of left side of the index ({1})
# and the sum of the right side of the index ({50,-51,1,1}) both equal 1.
#
# Last one:
# You are given the array {20,10,-80,10,10,15,35}
# At index 0 the left side is {}
# The right side is {10,-80,10,10,15,35}
# They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
# Index 0 is the place where the left side and right side are equal.

# 입력 == 출력
# Test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
# Test.assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
# Test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
# Test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
# Test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
# Test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
# Test.assert_equals(find_even_index(list(range(1,100))),-1)
# Test.assert_equals(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
# Test.assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
# Test.assert_equals(find_even_index(list(range(-100,-1))),-1)

# --------------------------
# 한글로 설명하기가 더 어려운 문제
# --------------------------

# My Code
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

# Warriors Code
def find_even_index_(arr):
    r = [i for i in range(len(arr)) if sum(arr[0:i]) == sum(arr[i+1:])]
    return r[0] if r else -1

if __name__=='__main__':
    answer = find_even_index([1, 2, 3, 4, 3, 2, 1])
    print(answer)