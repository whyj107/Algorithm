# Are arrow functions odd?
# https://www.codewars.com/kata/559f80b87fa8512e3e0000f5/train/python

# 나의 풀이
def odds(values):
    return [v for v in values if v%2!=0]

# 다른 사람의 풀이
def odds1(values):
    return [i for i in values if i % 2]

odds2 = lambda o: [i for i in o if i % 2 != 0]

print(odds([]), [])
print(odds([2, 4, 6]), [])
print(odds([1, 3, 5]), [1, 3, 5])
print(odds([1, 2, 3, 4, 5, 6]), [1, 3, 5])