# 문제
# Python is now supported on Codewars!
# For those of us who are not very familiar with Python,
# let's handle the very basic challenge of creating a class named Python.
# We want to give our Pythons a name, so it should take a name argument that we can retrieve later.

# 입력 == 출력
# bubba = Python('Bubba')
# bubba.name # should return 'Bubba'

# --------------------------
# 클래스(class) : 과자 틀
# 객체(object) : 과자 틀에 의해서 만들어진 과자
# def setdata(self, first, second):         메서드의 매개변수
#   self.first = first                      메서드의 수행문
#   self.second = second                    메서드의 수행문

# a.setdata(4, 2)
# self = a
# a.first = 4
# a.second =2
# --------------------------

# My Code
class Python(object):
    def __init__(self, name):
        self.name = name

if __name__=='__main__':
    bubba = Python('Bubba')
    print(bubba.name)