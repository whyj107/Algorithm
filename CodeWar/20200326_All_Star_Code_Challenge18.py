# 문제
# This Kata is intended as a small challenge for my students
# All Star Code Challenge #18
# Create a function called that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.
#
# If no occurrences can be found, a count of 0 should be returned.
#
# strCount('Hello', 'o') // => 1
# strCount('Hello', 'l') // => 2
# strCount('', 'z')      // => 0
# Notes:
#
# The first argument can be an empty string
# The second string argument will always be of length 1

# 입력 == 출력
# test.assert_equals(str_count('hello', 'l'), 2)

# --------------------------
# count를 사용하면 어렵지 않을 것 같다.
# --------------------------

# My Code
def str_count(strng, letter):
    return strng.count(letter)

if __name__=='__main__':
    answer = str_count('Hello', 'l')
    print(answer)