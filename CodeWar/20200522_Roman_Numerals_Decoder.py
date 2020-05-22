# 문제
# Roman Numerals Decoder
# Create a function that takes a Roman numeral as its argument
# and returns its value as a numeric decimal integer.
# You don't need to validate the form of the Roman numeral.
#
# Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately,
# starting with the leftmost digit and skipping any 0s.
# So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC)
# and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII).
# The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

# 입력 == 출력
# test.assert_equals(solution('XXI'), 21, 'XXI should == 21')
# test.assert_equals(solution('I'), 1, 'I should == 1')
# test.assert_equals(solution('IV'), 4, 'IV should == 4')
# test.assert_equals(solution('MMVIII'), 2008, 'MMVIII should == 2008')
# test.assert_equals(solution('MDCLXVI'), 1666, 'MDCLXVI should == 1666')

# My Code
def solution(roman):
    n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    answer = 0
    for i in range(0, len(roman) - 1):
        if n[roman[i]] >= n[roman[i + 1]]:
            answer += n[roman[i]]
        else:
            answer -= n[roman[i]]
    return answer + n[roman[-1]]

if __name__ == '__main__':
    print(solution('XXI'), 21)
    print(solution('I'), 1)
    print(solution('IV'), 4)
    print(solution('MMVIII'), 2008)
    print(solution('MDCLXVI'), 1666)