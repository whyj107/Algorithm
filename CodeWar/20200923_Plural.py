# 문제
# Plural
# https://www.codewars.com/kata/52ceafd1f235ce81aa00073a/train/python

# 나의 풀이
def plural(n):
    return False if n == 1 else True

# 다른 사람의 풀이
def plural1(n):
    return n != 1

print(plural(0),     True,  "Plural for 0"    )
print(plural(0.5),   True,  "Plural for 0.5"  )
print(plural(1),     False, "1 is singular!"  )
print(plural(100),   True,  "Plural for 100"  )