# All unique
# https://www.codewars.com/kata/553e8b195b853c6db4000048/train/python

# 나의 풀이
def has_unique_chars(string):
    return len(string) == len(set(string))

print(has_unique_chars("abcdef"), True)
print(has_unique_chars("++-"), False)
print(has_unique_chars("  nAa"), False)
