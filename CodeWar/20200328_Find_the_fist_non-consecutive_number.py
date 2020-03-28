# 문제
# Your task is to find the first element of an array that is not consecutive.
# By not consecutive we mean not exactly 1 larger than the previous element of the array.
# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive
# but 6 is not, so that's the first non-consecutive number.
# If the whole array is consecutive then return null2.
# The array will always have at least 2 elements1 and all elements will be numbers.
# The numbers will also all be unique and in ascending order.
# The numbers could be positive or negative and the first non-consecutive could be either too!

# 입력 == 출력
# Test.assert_equals(first_non_consecutive([1,2,3,4,6,7,8]), 6)
# Test.assert_equals(first_non_consecutive([1,2,3,4,5,6,7,8]), None)
# Test.assert_equals(first_non_consecutive([4,6,7,8,9,11]), 6)
# Test.assert_equals(first_non_consecutive([4,5,6,7,8,9,11]), 11)
# Test.assert_equals(first_non_consecutive([31,32]), None)
# Test.assert_equals(first_non_consecutive([-3,-2,0,1]), 0)
# Test.assert_equals(first_non_consecutive([-5,-4,-3,-1]), -1)

# --------------------------
# 시간이 오래걸렸다... 반성하자.
# --------------------------

# My Code
def first_non_consecutive(arr):
    if len(arr) > 2:
        for i in range(1, len(arr)-1):
            if arr[i] - arr[i - 1] != arr[i + 1] - arr[i]:
                if arr[i + 1] != arr[-1] and arr[i+2] - arr[i+1] != arr[i] - arr[i-1]:
                    return arr[i]
                return arr[i+1]
    return None

# Warriors Code
def first_non_consecutive_(arr):
    if not arr: return 0
    for i, x in enumerate(arr[:-1]):
        if x + 1 != arr[i + 1]:
            return arr[i + 1]

if __name__=='__main__':
    answer = first_non_consecutive([4, 6, 7, 8, 9, 11])         # 6
    print(answer)
    answer = first_non_consecutive([4, 5, 6, 7, 8, 9, 11])      # 11
    print(answer)
    answer = first_non_consecutive([-3, -2, 0, 1])              # 0
    print(answer)
    answer = first_non_consecutive([-5, -4, -3, -1])            # -1
    print(answer)