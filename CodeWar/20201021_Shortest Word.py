# Shortest Word
# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

# 나의 풀이
def find_short(s):
    return min([len(i) for i in s.split(' ')])

print(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
print(find_short("turns out random test cases are easier than writing out basic ones"), 3)
print(find_short("lets talk about javascript the best language"), 3)
print(find_short("i want to travel the world writing code one day"), 1)
print(find_short("Lets all go on holiday somewhere very cold"), 2)



