# 문제
# Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# 입력 == 출력
# test.assert_equals(solution(10), 23)

# My Code
def solution(number):
    return sum(set([i for i in range(1, number) if i % 3 == 0 or i % 5 == 0]))

if __name__=='__main__':
    print(solution(10))
    print(solution(20), 78)
    print(solution(200), 9168)