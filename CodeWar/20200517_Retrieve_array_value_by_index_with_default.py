# 문제
# Retrieve array value by index with default
# Complete the solution.
# It should try to retrieve the value of the array at the index provided.
# If the index is out of the array's max bounds then it should return the default value instead.

# 입력 == 출력
# rng = list(range(1, 4))
# test.assert_equals(solution(rng, 1, 'a'), 2)
# test.assert_equals(solution(rng, -1, 'a'), 3)
# test.assert_equals(solution(rng, -5, 'a'), 'a')
# test.assert_equals(solution(rng, -3, 'a'), 1)
#
# rng = list(range(1, 6))
# test.assert_equals(solution(range(1,6), 10, 'a'), 'a')
# test.assert_equals(solution([None, None], 0, 'a'), None)

# My Code
def solution(items, index, default_value):
    try:
        return items[index]
    except:
        return default_value

def solution1(items, index, default_value):
    return items[index] if -len(items) <= index < len(items) else default_value

if __name__=='__main__':
    rng = list(range(1, 4))
    print(solution(rng, 1, 'a'), 2)
    print(solution(rng, -1, 'a'), 3)
    print(solution(rng, -5, 'a'), 'a')
    print(solution(rng, -3, 'a'), 1)
