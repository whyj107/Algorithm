# 문제
# Valid Phone Number
# Write a function that accepts a string, and returns true
# if it is in the form of a phone number.
# Assume that any integer from 0-9 in any of the spots will produce a valid phone number.
#
# Only worry about the following format:
# (123) 456-7890 (don't forget the space after the close parentheses)

# 입력 == 출력
# Test.assert_equals(validPhoneNumber("(123) 456-7890"), True)

# My Code
import re
def validPhoneNumber(phoneNumber):
    return False if re.match('\(\d{3}\) \d{3}-\d{4}', phoneNumber) == None else (True if len(phoneNumber) == 14 else False)

# Warriors Code
def validPhoneNumber1(phoneNumber):
    return bool(re.match(r"^(\([0-9]+\))? [0-9]+-[0-9]+$", phoneNumber))

if __name__ == '__main__':
    print(validPhoneNumber("(123) 456-7890"), True)
    print(validPhoneNumber("(123) 456-7890abc"), False)