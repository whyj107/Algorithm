# 문제
# Basic Calculator
# https://www.codewars.com/kata/5296455e4fe0cdf2e000059f/train/python

# 나의 풀이
def calculate(num1, operation, num2):
    dic = {"+": lambda a, b: a+b,
           "-": lambda a, b: a-b,
           "*": lambda a, b: a*b,
           "/": lambda a, b: a/b}
    try:
        return dic[operation](num1, num2)
    except:
        return None

# 다른 사람의 풀이
def calculate1(num1, operation, num2):
    try:
        return eval("{} {} {}".format(num1, operation, num2))
    except (ZeroDivisionError, SyntaxError):
        return None

if __name__ == '__main__':
    print(calculate(3.2, "+", 8), 11.2, "3.2 + 8 = 11.2")
    print(calculate(3.2, "-", 8), -4.8, "3.2 - 8 = -4.8")
    print(calculate(3.2, "/", 8), 0.4, "3.2 / 8 = .4")
    print(calculate(3.2, "*", 8), 25.6, "3.2 * 8 = 25.6")
    print(calculate(-3, "+", 0), -3, "-3 + 0 = -3")
    print(calculate(-3, "-", 0), -3, "-3 - 0 = -3")
    print(calculate(-2, "/", -2), 1, "-2 / -2 = 1")
    print(calculate(-3, "*", 0), 0, "-3 * 0 = 0")
    print(calculate(-3, "/", 0), None, "-3 / 0 = None")
    print(calculate(-3, "w", 0), None, "-3 w 0 = None")
    print(calculate(-3, "w", 1), None, "-3 w 1 = None")
