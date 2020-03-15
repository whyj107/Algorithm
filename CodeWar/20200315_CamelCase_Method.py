# 문제
# Write simple .camelCase method (camel_case function in PHP, CamelCase in C#
# or camelCase in Java) for strings.
# All words must have their first letter capitalized without spaces.

# 입력 == 출력
# Test.describe("Basic tests")
# Test.assert_equals(camel_case("test case"), "TestCase")
# Test.assert_equals(camel_case("camel case method"), "CamelCaseMethod")
# Test.assert_equals(camel_case("say hello "), "SayHello")
# Test.assert_equals(camel_case(" camel case word"), "CamelCaseWord")
# Test.assert_equals(camel_case(""), "")

# --------------------------
# title과 replace를 섞어서 쓰면 간단한 문제!!
# --------------------------

# My Code
def camel_case(string):
    return string.title().replace(" ", "")

# Warriors Code
def camel_case_(string):
    return ''.join((string.title()).split())

if __name__=='__main__':
    answer = camel_case("test case")
    print(answer)
    answer = camel_case("camel case method")
    print(answer)
    answer = camel_case("say hello ")
    print(answer)
    answer = camel_case(" camel case word")
    print(answer)
    answer = camel_case("")
    print(answer)