# 문제
# Strip Comments
# Complete the solution so that it strips all text
# that follows any of a set of comment markers passed in.
# Any whitespace at the end of the line should also be stripped out.

# 입력 == 출력
# Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
# Test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")

# My Code
def solution(string, markers):
    if string == "":
        return ""
    answer = []
    for i in string.split('\n'):
        pre_idx = 9999
        for j in markers:
            idx = i.find(j)
            if idx != -1:
                pre_idx = min(pre_idx, idx)
        if pre_idx != -1 and pre_idx < len(i):
            answer.append(i[:pre_idx])
        else:
            answer.append(i)

    answer1 = []
    for i in answer:
        if len(i) > 0:
            if i[-1] == ' ':
                answer1.append(i[:-1])
            else:
                answer1.append(i)
        else:
            answer1.append('')
    return '\n'.join(answer1)

# Warriors Code
def solution1(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)


if __name__=='__main__':
    # print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
    # print("apples, pears\ngrapes\nbananas")
    # print(solution('apples, pears # and bananas\ngrapes\nbananas !#apples', ['#', '!']))
    # print('apples, pears\ngrapes\nbananas')
    # print(solution('\n#', ['#', '!']))
    # print(solution('#', ['#', '!']))
    print(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")