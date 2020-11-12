# String doubles
# https://www.codewars.com/kata/5a145ab08ba9148dd6000094/train/python

# 나의 풀이
def doubles(s):
    for i in s:
        if i*2 in s:
            s = s.replace(i*2, '')
    return s

# 다른 사람의 풀이
def doubles1(s):
    cs = []
    for c in s:
        if cs and cs[-1] == c:
            cs.pop()
        else:
            cs.append(c)
    return ''.join(cs)

print(doubles('abbbzz'),'ab')
print(doubles('zzzzykkkd'),'ykd')
print(doubles('abbcccdddda'),'aca')
print(doubles('vvvvvoiiiiin'),'voin')
print(doubles('rrrmooomqqqqj'),'rmomj')
print(doubles('xxbnnnnnyaaaaam'),'bnyam')    