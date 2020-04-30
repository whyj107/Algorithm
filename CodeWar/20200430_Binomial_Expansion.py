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
        c = int(tmp[1])
        tmp_b = [[] for _ in range(c + 1)]
        tmp_b[0] = [1, 1]
        for i in range(1, len(tmp_b)):
            tmp_b[i].append(1)
            for j in range(i-1):
                tmp_b[i].append(tmp_b[i-1][j]+tmp_b[i-1][j+1])
            tmp_b[i].append(1)
        # [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]
        # print(tmp_b[-1])

        a = 1
        x = ''
        b = 1

        if tmp[0].count('-') == 2:
            tmp[0] = tmp[0].split('-')
            if tmp[0][0] == '':
                a = -1
            else:
                a = int(tmp[0][0])

            x = tmp[0][1]
            b = int(tmp[0][2])

        elif tmp[0].count('-') == 1:
            if tmp[0].count('+') == 1:
                tmp[0] = tmp[0].split('+')
                a = int(tmp[0][0][:-1])
                x = tmp[0][0][-1]
                b = int(tmp[0][1])
            else:
                tmp[0] = tmp[0].split('-')
                if len(tmp[0][0]) > 1:
                    a = int(tmp[0][0][:-1])
                else:
                    a = 1
                x = tmp[0][0][-1]
                b = - int(tmp[0][1])
        else:
            tmp[0] = tmp[0].split('+')
            if len(tmp[0][0]) > 1:
                a = int(tmp[0][0][:-1])
            else:
                a = 1
            x = tmp[0][0][-1]
            b = int(tmp[0][1])

        answer = ''
        cnt = int(tmp[1])
        for i in range(len(tmp_b[-1])):
            a_ = tmp_b[-1][i] * pow(a, cnt) * pow(b, c-cnt)
            if a_ == 1:
                print(x + '^' + str(cnt))
            else:
                print(str(a_) + x + '^' + str(cnt))
            cnt -= 1

    return '--------------'

if __name__=='__main__':
    # print(expand("(x-1)^0"))
    # print(expand("(x-1)^1"))
    print(expand("(-x-1)^2"))
    print(expand("(x-1)^2"))
    print(expand("(x+1)^2"))
    # print(expand("(-2x+1)^2"))
    # print(expand("(2x-1)^2"))
    # print(expand("(5m+3)^4"))