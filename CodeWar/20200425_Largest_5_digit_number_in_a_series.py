# 문제
# In the following 6 digit number:
#
# 283910
# 91 is the greatest sequence of 2 consecutive digits.
#
# In the following 10 digit number:
#
# 1234567890
# 67890 is the greatest sequence of 5 consecutive digits.
#
# Complete the solution so that it returns the greatest sequence of five consecutive digits found within the number given.
# The number will be passed in as a string of only digits.
# It should return a five digit integer.
# The number passed may be as large as 1000 digits.

# 입력 == 출력
# test.expect(actual != 0, 'solution returned zero')
# test.expect(actual, 'solution did not return a value')
# test.assert_equals(actual, 99890, 'solution did not return correct value')
# test.assert_equals(solution('1234567898765'), 98765, 'Failed when max 5 digits is at end of number')

# My Code
def solution(digits):
    str_digits = str(digits)
    answer = []
    for i in range(len(str_digits)):
        answer.append(int(str_digits[i:i+5]))
    return max(answer)

if __name__=='__main__':
    print(solution(1234567898765))