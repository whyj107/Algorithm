# Two to One
# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

# 나의 풀이
def longest(a1, a2):
    return ''.join(sorted(list(set(a1+a2))))

# 다른 사람의 풀이
def longest1(a1, a2):
    return "".join(sorted(set(a1 + a2)))

print(longest("aretheyhere", "yestheyarehere"), "aehrsty")
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
print(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
