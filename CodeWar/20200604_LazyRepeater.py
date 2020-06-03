# 문제
# Lazy Repeater
# The makeLooper() function (make_looper in Python) takes a string (of non-zero length) as an argument. It returns a function. The function it
# returns will return successive characters of the string on successive invocations.
# It will start back at the beginning of the string once it reaches the end.

# 입력 == 출력
# abc = make_looper("abc")
#
# test.assert_equals(abc(), 'a')
# test.assert_equals(abc(), 'b')
# test.assert_equals(abc(), 'c')
#
# test.assert_equals(abc(), 'a')
# test.assert_equals(abc(), 'b')
# test.assert_equals(abc(), 'c')

# My Code
def make_looper(string):
    global idx
    idx = -1
    def solve():
        global idx
        idx += 1
        if idx == len(string):
            idx = 0
        return string[idx]
    return solve

from itertools import cycle

def make_looper1(string):
    g = cycle(string)
    return lambda: next(g)

class make_looper2(cycle):

    def __call__(self):
        return self.__next__()

if __name__ == '__main__':
    abc = make_looper("abc")

    print(abc(), 'a')
    print(abc(), 'b')
    print(abc(), 'c')

    print(abc(), 'a')
    print(abc(), 'b')
    print(abc(), 'c')