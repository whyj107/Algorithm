# 문제
# Float Precision
# Update the solution method to round the argument value to the closest precision of two.
# The argument will always be a float.

# 입력 == 출력
# Test.assert_equals(solution(2.34), 2.34)
# Test.assert_equals(solution(5.678), 5.68)

# My Code
def solution(n):
    return round(n, 2)

def solution1(n):
    return float('{:0.2f}'.format(n))

if __name__=='__main__':
    print(solution(2.34))
    print(solution(5.678))

    # solution = lambda x: round(x, 2)