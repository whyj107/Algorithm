# 문제
#

# 입력 == 출력
# Test.assert_equals(to_alternating_case("hello world"), "HELLO WORLD")
# Test.assert_equals(to_alternating_case("HELLO WORLD"), "hello world")
# Test.assert_equals(to_alternating_case("hello WORLD"), "HELLO world")
# Test.assert_equals(to_alternating_case("HeLLo WoRLD"), "hEllO wOrld")
# Test.assert_equals(to_alternating_case("12345"), "12345")
# Test.assert_equals(to_alternating_case("1a2b3c4d5e"), "1A2B3C4D5E")
# Test.assert_equals(to_alternating_case("String.prototype.toAlternatingCase"), "sTRING.PROTOTYPE.TOaLTERNATINGcASE")

# My Code
def to_alternating_case(string):
    answer =''
    for i in string:
        # 소문자이면 대문자로
        if i.isupper():
            answer += i.lower()
        # 대문자이면 소문자로
        elif i.islower():
            answer += i.upper()
        # 그 이외
        else:
            answer += i
    return answer

# Warriors Code
def to_alternating_case_(string):
    return string.swapcase()

if __name__=='__main__':
    answer = to_alternating_case_('hello world')
    print(answer)
    answer = to_alternating_case('HELLO WORLD')
    print(answer)
    answer = to_alternating_case('hello WORLD')
    print(answer)
    answer = to_alternating_case('HeLLo WoRLD')
    print(answer)
    answer = to_alternating_case('12345')
    print(answer)