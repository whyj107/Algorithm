# Switcheroo
# https://www.codewars.com/kata/57f759bb664021a30300007d/train/python

# 나의 풀이
def switcheroo(string):
    return string.translate(str.maketrans("ab", "ba"))

# 다른 사람의 풀이
def switcheroo1(string):
    return ((string.replace('a','x')).replace('b','a')).replace('x','b')

print(switcheroo("abc"), "bac")
print(switcheroo('aaabcccbaaa'), 'bbbacccabbb')
print(switcheroo('ccccc'), 'ccccc')
print(switcheroo('abababababababab'), 'babababababababa')
print(switcheroo('aaaaa'), 'bbbbb')