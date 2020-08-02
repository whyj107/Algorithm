# 문제
# Valid Parentheses
# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python

# 나의 풀이
def valid_parentheses(string):
    if string.count("(") == 0 and string.count(")") == 0:
        return True
    else:
        tmp = []
        for i in string:
            try:
                if i == "(":
                    tmp.append(i)
                elif i == ")":
                    tmp.pop()
            except:
                return False
        return len(tmp) == 0

# 다른 사람의 풀이
def valid_parentheses1(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False

if __name__ == '__main__':
    print(valid_parentheses("  ("), False)
    print(valid_parentheses(")test"), False)
    print(valid_parentheses("(boce(era)qrm)g(fk)qka()sy)(ag)btwzglt"), True)
    # print(valid_parentheses("hi())("), False)
    # print(valid_parentheses("hi(hi)()"), True)