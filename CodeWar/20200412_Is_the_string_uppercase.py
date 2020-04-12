# 문제
# Create a method is_uppercase() to see whether the string is ALL CAPS. For example:
#
# is_uppercase("c") == False
# is_uppercase("C") == True
# is_uppercase("hello I AM DONALD") == False
# is_uppercase("HELLO I AM DONALD") == True
# is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") == False
# is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") == True
# In this Kata, a string is said to be in ALL CAPS
# whenever it does not contain any lowercase letter
# so any string containing no letters at all is trivially considered to be in ALL CAPS.

# 입력 == 출력
# gen_test_case("c", False)
# gen_test_case("C", True)
# gen_test_case("hello I AM DONALD", False)
# gen_test_case("HELLO I AM DONALD", True)

# My Code
def is_uppercase(inp):
    for i in inp:
        if i.islower():
            return False
    return True

def is_uppercase1_(inp):
    return str.isupper(inp)

if __name__=='__main__':
    answer = is_uppercase("c")
    print(answer)
    answer = is_uppercase("C")
    print(answer)
    answer = is_uppercase("hello I Am DONALD")
    print(answer)
    answer = is_uppercase("HELLO I AM DONALD")
    print(answer)