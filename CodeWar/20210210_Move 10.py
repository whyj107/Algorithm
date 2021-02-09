# Move 10
# https://www.codewars.com/kata/57cf50a7eca2603de0000090/train/python

# 나의 풀이
def move_ten(st):
    a = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(a[(a.find(i)+10) % len(a)] for i in st)

# 다른 사람의 풀이
from string import ascii_lowercase as al
tbl = str.maketrans(al, al[10:] + al[:10])
def move_ten1(st):
    return st.translate(tbl)

def move_ten2(st):
    return ''.join(chr(ord(i)+10) if i<'q' else chr(ord(i)-16) for i in st)

print(move_ten("testcase"), "docdmkco")
print(move_ten("codewars"), "mynogkbc")
print(move_ten("exampletesthere"), "ohkwzvodocdrobo")
print(move_ten("returnofthespacecamel"), "bodebxypdroczkmomkwov")
print(move_ten("bringonthebootcamp"), "lbsxqyxdrolyydmkwz")
print(move_ten("weneedanofficedog"), "goxoonkxyppsmonyq")
