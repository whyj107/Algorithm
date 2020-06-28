# 문제
# Calculating with Functions
# This time we want to write calculations using functions and get the results.
# Let's have a look at some examples:
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations:
# plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand,
# the most inner function represents the right operand
# Divison should be integer division. For example, this should return 2, not 2.666666...:

# 입력 == 출력
# Test.assert_equals(seven(times(five())), 35)
# Test.assert_equals(four(plus(nine())), 13)
# Test.assert_equals(eight(minus(three())), 5)
# Test.assert_equals(six(divided_by(two())), 3)

# My Code
def zero(n=''): return calc(n+'0')
def one(n=''): return calc(n+'1')
def two(n=''): return calc(n+'2')
def three(n=''): return calc(n+'3')
def four(n=''): return calc(n+'4')
def five(n=''): return calc(n+'5')
def six(n=''): return calc(n+'6')
def seven(n=''): return calc(n+'7')
def eight(n=''): return calc(n+'8')
def nine(n=''): return calc(n+'9')

def plus(n1): return str(n1) + '+'
def minus(n1): return str(n1) + '-'
def times(n1): return str(n1) + '*'
def divided_by(n1): return str(n1) + '/'

def calc(a):
    if len(a) > 1:
        if a[1] == '+':
            return int(a[2]) + int(a[0])
        elif a[1] == '-':
            return int(a[2]) - int(a[0])
        elif a[1] == '*':
            return int(a[2]) * int(a[0])
        elif a[1] == '/':
            return int(a[2]) // int(a[0])
    else:
        return a

# Warriors Code
def zero1(f = None): return 0 if not f else f(0)
def one1(f = None): return 1 if not f else f(1)
def two1(f = None): return 2 if not f else f(2)
def three1(f = None): return 3 if not f else f(3)
def four1(f = None): return 4 if not f else f(4)
def five1(f = None): return 5 if not f else f(5)
def six1(f = None): return 6 if not f else f(6)
def seven1(f = None): return 7 if not f else f(7)
def eight1(f = None): return 8 if not f else f(8)
def nine1(f = None): return 9 if not f else f(9)

def plus1(y): return lambda x: x+y
def minus1(y): return lambda x: x-y
def times1(y): return lambda  x: x*y
def divided_by1(y): return lambda  x: x/y

if __name__ == "__main__":
    print(seven(times(five())), 35)
    print(four(plus(nine())), 13)
    print(eight(minus(three())), 5)
    print(six(divided_by(two())), 3)
