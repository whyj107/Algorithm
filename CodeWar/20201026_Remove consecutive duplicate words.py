# Remove consecutive duplicate words
# https://www.codewars.com/kata/5b39e91ee7a2c103300018b3/train/python

# 나의 풀이
def remove_consecutive_duplicates(s):
    pre = ''
    answer = []
    for i in s.split(' '):
        if pre != i:
            answer.append(i)
        pre = i
    return ' '.join(answer)

# 다른 사람의 풀이
from itertools import groupby

def remove_consecutive_duplicates1(s):
    return ' '.join(k for k,_ in groupby(s.split()))

print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'), 'alpha beta gamma delta alpha beta gamma delta');
