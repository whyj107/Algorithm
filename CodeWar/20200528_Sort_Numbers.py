# 문제
# Sort Numbers
# Finish the solution so that it sorts the passed in array of numbers.
# If the function passes in an empty array or null/nil value then it should return an empty array.

# 입력 == 출력
# test.assert_equals(solution([1,2,10,5]), [1,2,5,10])

# My Code
def solution(nums):
    if nums is not None:
        nums.sort()
        return nums
    else:
        return []

def solution1(nums):
    return sorted(nums) if nums else []

# solution = lambda l: sorted(l) if l else []

if __name__=='__main__':
    print(solution([1, 2, 10, 5]))
    print(solution(None))