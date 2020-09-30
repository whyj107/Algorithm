# 문제
# Simple Events
# https://www.codewars.com/kata/52d3b68215be7c2d5300022f/train/python

# 문제를 이해하기 힘들어서 다른 사람의 코드를 보고 이해했다.
class Event(object):
    def __init__(self):
        self.handlers = set()

    def subscribe(self, func):
        self.handlers.add(func)

    def unsubscribe(self, func):
        self.handlers.remove(func)

    def emit(self, *args, **kwargs):
        for func in self.handlers:
            func(*args, **kwargs)