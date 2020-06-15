# 문제
# Arabian String
# You must create a method that can convert a string from any format into CamelCase.
# This must support symbols too.
#
# Don't presume the separators too much or you could be surprised.

# 입력 == 출력
# Test.assert_equals(camelize("java script"),"JavaScript" )
# Test.assert_equals(camelize("cODE warS"),"CodeWars" )

# My Code
import re
def camelize(str_):
    return ''.join([i.capitalize() for i in re.sub('[^0-9a-zA-Z]', ' ', str_).split(' ')])

# Warriors Code
def camelize1(s):
    return "".join([w.capitalize() for w in re.split("\W|_", s)])

if __name__ == '__main__':
    # print(camelize("java script"), "JavaScript")
    # print(camelize("cODE warS"), "CodeWars")
    print(camelize("pQdW gUtLjzju GwSIP40!QD4bJV6jSdS1"), "PqdwGutljzjuGwsip40Qd4bjv6jsds1")