# 문제
# Convert string to camel case
# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized
# only if the original word was capitalized (known as Upper Camel Case,
# also often referred to as Pascal case).

# 입력 == 출력
# test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
# test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
# test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
# test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")

# My Code
def to_camel_case(text):
    if text == '':
        return ''
    answer = text.title().replace('-', '').replace('_', '')
    return text[0] + answer[1:]

# Warriors Code
def to_camel_case1(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s

if __name__ == '__main__':
    print(to_camel_case(''), '')
    print(to_camel_case("the_stealth_warrior"), "theStealthWarrior")
    print(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior")
    print(to_camel_case("A-B-C"), "ABC")