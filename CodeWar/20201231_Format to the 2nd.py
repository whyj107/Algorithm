# Format to the 2nd
# https://www.codewars.com/kata/58311faba317216aad000168/train/python

# 나의 풀이
def print_nums(*input_):
    lst = list(input_)
    if len(lst) == 0 : return ''
    max_len = max(len(str(i)) for i in lst)
    return '\n'.join(str(i).zfill(max_len) for i in lst)

# 다른 사람의 풀이
def print_nums1(*num):
    return "\n".join([str(x).zfill(len(str(max(num)))) for x in num])

print(print_nums(), '')
print(print_nums(2), '2')
print(print_nums(1, 12, 34), '01\n12\n34')
print(print_nums(1009, 2), '1009\n0002')
