# 문제
# Reversed Words
# Complete the solution
# so that it reverses all of the words within the string passed in.

# 입력 == 출력
# test.assert_equals(reverseWords("hello world!"), "world! hello")

# My Code
def reverseWords(str):
    return " ".join(reversed(str.split(" ")))

# Warriors Code
def reverseWords1(str):
    return " ".join(str.split(" ")[::-1])

if __name__ == '__main__':
    print(reverseWords("hello world!"), "word! hello")