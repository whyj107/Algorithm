# Numbers to Letters
# https://www.codewars.com/kata/57ebaa8f7b45ef590c00000c/train/python

# 나의 풀이
def switcher(arr):
    dic = {'27': '!', '28': '?', '29': ' ', '0': ''}
    return ''.join(chr(123-int(a)) if 0 < int(a) < 27 else dic[a] for a in arr)

# 다른 사람의 풀이
import string
letters = string.ascii_lowercase[::-1] + '!? '
def switcher1(arr):
    return ''.join([letters[ch-1] for ch in map(int, arr) if ch])

print(switcher(['24', '12', '23', '22', '4', '26', '9', '8']), 'codewars')
print(switcher(['25', '7', '8', '0', '4', '14', '23', '8', '25', '23', '29', '16', '16', '4']), 'btswmdsbd kkw')
print(switcher(['4', '24']), 'wc')
print(switcher(['12']), 'o')
print(switcher(['12', '28', '25', '21', '25', '7', '11', '22', '0', '15']), 'o?bfbtpel')