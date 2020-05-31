# 문제
# Round by 0.5 steps
# Round any given number to the closest 0.5 step
# Round up if number is as close to previous and next 0.5 steps.

# 입력 == 출력
# Test.assert_equals(solution(4.2), 4)
# Test.assert_equals(solution(4.25), 4.5)
# Test.assert_equals(solution(4.4), 4.5)
# Test.assert_equals(solution(4.6), 4.5)
# Test.assert_equals(solution(4.75), 5)
# Test.assert_equals(solution(4.8), 5)

# My Code
def solution(n):
    answer = (n * 10) % 10
    if 2.5 <= answer < 7.5:
        answer = 0.5
    else:
        answer = 0

    return round(n*2)//2 + answer

# Warriors Code
def solution1(n):
    return round(2 * n) / 2

if __name__ == '__main__':
    print(solution(4.2), 4)
    print(solution(4.25), 4.5)
    print(solution(4.4), 4.5)
    print(solution(4.6), 4.5)
    print(solution(4.75), 5)
    print(solution(4.8), 5)