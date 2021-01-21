# String array duplicates
# https://www.codewars.com/kata/59f08f89a5e129c543000069/train/python

# 나의 풀이
def dup(arry):
    result = []
    for a in arry:
        pre = a[0]
        tmp = [pre]
        for i in range(1, len(a)):
            if pre != a[i]:
                tmp.append(a[i])
            pre = a[i]
        result.append(''.join(tmp))
    return result

# 다른 사람의 풀이
from itertools import groupby
def dup1(arry):
    return ["".join(c for c, grouper in groupby(i)) for i in arry]

import re
def dup2(arry):
    return list(map(lambda s: re.sub(r'(\w)\1+', r'\1', s), arry))


print(dup(["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]),
      ['codewars','picaniny','hubububo'])
# print(dup(["abracadabra","allottee","assessee"]),['abracadabra','alote','asese'])
# print(dup(["kelless","keenness"]), ['keles','kenes'])
# print(dup(["Woolloomooloo","flooddoorroommoonlighters","chuchchi"]), ['Wolomolo','flodoromonlighters','chuchchi'])
# print(dup(["adanac","soonness","toolless","ppellee"]), ['adanac','sones','toles','pele'])
# print(dup(["callalloo", "feelless", "heelless"]), ['calalo', 'feles', 'heles'])
# print(dup(["putteellinen", "keenness"]), ['putelinen', 'kenes'])
# print(dup(["kelless", "voorraaddoosspullen", "achcha"]), ['keles','voradospulen','achcha'])