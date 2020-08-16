# 문제
# Who has the most money?
# https://www.codewars.com/kata/528d36d7cc451cd7e4000339/train/python

# 나의 풀이
def most_money(students):
    d = {i.name: i.fives * 5 + i.tens*10 + i.twenties*20 for i in students}
    tmp = list(set([i.fives * 5 + i.tens*10 + i.twenties*20 for i in students]))
    return "all" if len(tmp) == 1 and len(students) != 1 else max(d.keys(), key=(lambda k: d[k]))

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

if __name__ == '__main__':
    phil = Student("Phil", 2, 2, 1)
    cam = Student("Cameron", 2, 2, 0)
    geoff = Student("Geoff", 0, 3, 0)

    print(most_money([cam, geoff, phil]), "Phil")
    print(most_money([cam, geoff]), "all")
    print(most_money([geoff]), "Geoff")