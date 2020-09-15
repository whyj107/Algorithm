# 문제
# Sleigh Authentication
# https://www.codewars.com/kata/52adc142b2651f25a8000643/train/python

# 나의 풀이
class Sleigh(object):
    def authenticate(self, name, password):
        return name is 'Santa Claus' and password is 'Ho Ho Ho'

# 다른 사람의 풀이
class Sleigh(object):
    def authenticate(self, name, password):
        return (name, password) == ('Santa Claus', 'Ho Ho Ho!')