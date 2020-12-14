# Valid Spacing
# https://www.codewars.com/kata/5f77d62851f6bc0033616bd8/train/python

# 나의 풀이
def valid_spacing(s):
    return '' not in s.split(' ') or ''==s

# 다른 사람의 풀이
def valid_spacing1(s):
    return s == ' '.join(s.split())

print(valid_spacing('Hello world'),True)
print(valid_spacing(' Hello world'),False)
print(valid_spacing('Hello  world '),False)
print(valid_spacing('Hello'),True)
print(valid_spacing('Helloworld'),True)
print(valid_spacing(''), True)
print(valid_spacing(' '), False)