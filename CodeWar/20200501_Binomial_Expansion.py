# 문제
# The purpose of this kata is to write a program that can do some algebra.
# Write a function expand that takes in an expresion with a single, one character variable, and expands it.
# The expresion is in the form (ax+b)^n where a and b are integers
# which may be positive or negative, x is any one character long variable, and n is a natural number.
# If a = 1, no coeficient will be placed in front of the variable.
# If a = -1, a "-" will be placed in front of the variable.
#
# The expanded form should be returned as a string in the form ax^b+cx^d+ex^f...
# where a, c, and e are the coefficients of the term, x is the original one character variable
# that was passed in the original expression and b, d, and f, are the powers
# that x is being raised to in each term and are in decreasing order.
# If the coeficient of a term is zero, the term should not be included.
# If the coeficient of a term is one, the coeficient should not be included.
# If the coeficient of a term is -1, only the "-" should be included.
# If the power of the term is 0, only the coeficient should be included.
# If the power of the term is 1, the carrot and power should be excluded.

# 입력 == 출력
# Test.assert_equals(expand("(x-1)^0"), "1")
# Test.assert_equals(expand("(x-1)^1"), "x-1")
# Test.assert_equals(expand("(x-1)^2"), "x^2-2x+1")
#
# Test.assert_equals(expand("(5m+3)^4"), "625m^4+1500m^3+1350m^2+540m+81")
# Test.assert_equals(expand("(2x-3)^3"), "8x^3-36x^2+54x-27")
# Test.assert_equals(expand("(7x-7)^0"), "1")

# My Code
def expand(expr):
    tmp = expr.replace('(', '').replace(')', '').split('^')
    if tmp[1] == str(0):
        return str(1)
    elif tmp[1] == str(1):
        return tmp[0]
    else:
        # c 추출
        c = int(tmp[1])

        # 제곱시에 필요한 상수 값
        tmp_b = [[] for _ in range(c + 1)]
        tmp_b[0] = [1, 1]
        for i in range(1, len(tmp_b)):
            tmp_b[i].append(1)
            for j in range(i-1):
                tmp_b[i].append(tmp_b[i-1][j]+tmp_b[i-1][j+1])
            tmp_b[i].append(1)

        x = ''
        x_index = 0

        # x 추출
        for i in tmp[0]:
            if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
                x_index = tmp[0].find(i)
                x = tmp[0][x_index]
                break

        # a 추출
        a = tmp[0][:x_index]
        if a == '-':
            a = int(-1)
        elif a == '':
            a = int(1)
        else:
            a = int(tmp[0][:x_index])

        # b 추출
        b = int(tmp[0][x_index + 1:])

        cnt = c
        answer_list = []
        for i in tmp_b[-1]:
            a_tmp = i * pow(a, cnt) * pow(b, c-cnt)

            if cnt == 0:
                answer_list.append(str(a_tmp))
            elif cnt == 1:
                answer_list.append(str(a_tmp) + x)
            else:
                if a_tmp == 1:
                    answer_list.append(x + '^' + str(cnt))
                elif a_tmp == -1:
                    answer_list.append('-' + x + '^' + str(cnt))
                else:
                    answer_list.append(str(a_tmp) + x + '^' + str(cnt))
            cnt -= 1

        answer = answer_list[0]
        for i in range(1, len(answer_list)):
            if answer_list[i][0] == '-':
                answer += answer_list[i]
            else:
                answer += ('+' + answer_list[i])

    return answer

if __name__=='__main__':
    print(expand("(x-1)^0"))
    print(expand("(x-1)^1"))
    print(expand("(x-1)^2"))
    print(expand("(5m+3)^4"))
    print(expand("(2x-3)^3"))
    print(expand("(7x-7)^0"))