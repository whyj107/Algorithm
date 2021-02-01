# FIXME Get Full Name
# https://www.codewars.com/kata/597c684822bc9388f600010f/train/python

# 나의 풀이
class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}' if self.first_name != '' and self.last_name != '' else (self.last_name if self.first_name == '' else self.first_name)

# 다른 사람의 풀이
class Dinglemouse1(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_full_name(self):
        return (self.first_name + ' ' + self.last_name).strip()

print(Dinglemouse('Clint', 'Eastwood').get_full_name(), 'Clint Eastwood')
print(Dinglemouse('', 'Eastwood').get_full_name(), 'Eastwood')
print(Dinglemouse('Clint', '').get_full_name(), 'Clint')
print(Dinglemouse('', '').get_full_name(), '')