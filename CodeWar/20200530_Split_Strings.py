# 문제
# Split Strings
# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then
# it should replace the missing second character of the final pair with an underscore ('_').

# 입력 == 출력
# tests = (
#     ("asdfadsf", ['as', 'df', 'ad', 'sf']),
#     ("asdfads", ['as', 'df', 'ad', 's_']),
#     ("", []),
#     ("x", ["x_"]),
# )
#
# for inp, exp in tests:
#     test.assert_equals(solution(inp), exp)

# My Code
def solution(s):
    if len(s) % 2 != 0:
        s += '_'
    return [s[i] + s[i+1] for i in range(0, len(s), 2)]

# Warriors Code
import re

def solution1(s):
    return re.findall(".{2}", s + "_")

if __name__ == '__main__':
    tests = (
        ("asdfadsf", ['as', 'df', 'ad', 'sf']),
        ("asdfads", ['as', 'df', 'ad', 's_']),
        ("", []),
        ("x", ["x_"]),
    )

    for inp, exp in tests:
        print(solution(inp), exp)