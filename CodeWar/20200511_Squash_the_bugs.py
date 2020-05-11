# 문제
# Simple challenge
# - eliminate all bugs from the supplied code so that the code runs
# and outputs the expected value.
# Output should be the length of the longest word, as a number.
#
# There will only be one 'longest' word.

# 입력 == 출력
# Test.assert_equals(find_longest("The quick white fox jumped around the massive dog"), 7)
# Test.assert_equals(find_longest("Take me to tinseltown with you"), 10)
# Test.assert_equals(find_longest("Sausage chops"), 7)
# Test.assert_equals(find_longest("Wind your body and wiggle your belly"), 6)
# Test.assert_equals(find_longest("Lets all go on holiday"), 7)

# My Code
def find_longest(string):
    return max([len(i) for i in string.split(' ')])
    return max(map(len, string.split()))

if __name__=='__main__':
    print(find_longest("The quick white fox jumped around the massive dog"))