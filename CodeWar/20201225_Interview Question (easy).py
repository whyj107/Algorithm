# Interview Question (easy)
# https://www.codewars.com/kata/5b358a1e228d316283001892/train/python

# 나의 풀이
def get_strings(city):
    dic = {c: '*'*city.lower().count(c) for c in city.lower() if not c is ' '}
    return ','.join(f'{k}:{v}' for k, v in dic.items())

# 다른 사람의 풀이
from collections import Counter
def get_strings1(city):
    return ",".join(f"{char}:{'*'*count}" for char, count in Counter(city.replace(" ", "").lower()).items())

print(get_strings("Chicago") == "c:**,h:*,i:*,a:*,g:*,o:*")
print(get_strings("Bangkok") == "b:*,a:*,n:*,g:*,k:**,o:*")
print(get_strings("Las Vegas") == "l:*,a:**,s:**,v:*,e:*,g:*")