# 문제
# Sort the Gift Code
# https://www.codewars.com/kata/52aeb2f3ad0e952f560005d3/train/python

# 나의 풀이
def sort_gift_code(code):
    tmp = [c for c in code]
    tmp.sort()
    return ''.join(tmp)

# 다른 사람의 풀이
def sort_gift_code1(code):
    return "".join(sorted(code))

print(sort_gift_code('abcdef'), 'abcdef');
print(sort_gift_code('pqksuvy'), 'kpqsuvy');
print(sort_gift_code('zyxwvutsrqponmlkjihgfedcba'), 'abcdefghijklmnopqrstuvwxyz');