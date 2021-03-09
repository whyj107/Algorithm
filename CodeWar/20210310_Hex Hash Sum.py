# Hex Hash Sum
# https://www.codewars.com/kata/5ab363ff6a176b29880000dd/train/python

# 나의 풀이
def hex_hash(code):
    return sum(int(i) for c in code for i in format(ord(c), 'x') if i.isdecimal())

# 다른 사람의 풀이
def hex_hash1(code):
    return sum(int(d) for c in code for d in hex(ord(c)) if d.isdigit())

print(hex_hash("Yo"), 20)
# print(hex_hash('kcxnjsklsHskjHDkl7878hHJk'), 218)
# print(hex_hash(''), 0)
# print(hex_hash('ThisIsATest!'), 120)
# print(hex_hash('dhsajkbfyewquilb4y83q903ybr8q9apf7\9ph79qw0-eq230br[wq87r0=18-[#20r370B 7Q0RFP23B79037902RF79WQ0[]]]'), 802)