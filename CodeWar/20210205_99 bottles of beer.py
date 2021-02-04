# 99 bottles of beer
# https://www.codewars.com/kata/52a723508a4d96c6c90005ba/train/python

# 다른 사람의 풀이
def sing1():
    lst = []
    for i in range(97):
        lst.append(f'{99 - i} bottles of beer on the wall, {99 - i} bottles of beer.')
        lst.append(f'Take one down and pass it around, {98 - i} bottles of beer on the wall.')
    return lst + ['2 bottles of beer on the wall, 2 bottles of beer.', 'Take one down and pass it around, 1 bottle of beer on the wall.', '1 bottle of beer on the wall, 1 bottle of beer.', 'Take one down and pass it around, no more bottles of beer on the wall.', 'No more bottles of beer on the wall, no more bottles of beer.', 'Go to the store and buy some more, 99 bottles of beer on the wall.']

# 신기하다....
s="""/Td6WFoAAATm1rRGAgAhARYAAA
B0L+Wj4FwiAi5dABzgfMRvOiayBchkwC
oTnRZueVwweCaCOzkpl7lW+8i2w1DOJI
4QcafLbiSrQqJUu+CovkOtJdZX3ZZ6JYuAey
C0zroAqZGK5Fn1rDOTcLS50dUl1hWMsr3UEhpMM
S2OjjP87tLp1XrCTIweITpDTTIrL/FEv    UwiRb
I9ifMnEWlHTz7F1liMTi8WuQeXUIs8pG     dZxL
jWHqnoFDG/d9XAqWCmL8ipbLgqX0omMB     0BMFy
qU4xJqMgt6TrTEpmzfygGNFJcrdQimxl     upT/i
KsZLcZvyqWMrBxl56g6I27P80dQXtPLx     EAQRp
R75WiNNcVIPnyYb0Mfu2toVW6Bgtsofl     +DJX8
HMImBzc0LS1kjyzGLD4NJNPt/oc6IlJF     HiPIR
eap9D/zjMQqDG4lzuyr80F5BLqNu9GYJ     Tki2C
SgWwsOXd8cVsN7MKrCwQctJ5aYUd6n95     /bOwb
w7Th1RvcDF/v3fKccZwnNYxKi8hktKZ1   QPuOwn
CfXffmCpTQMuYDpOpRLkYntKkJ0OojsEOFXXDpH2
gRITmfrTzFVKnNGzdpfoHP686k0SnPjzvOYglQ
Mdm8gk3EXM33JlnBUXvfc6/n62Kl28I/
Wph+FVxmJupWMzjY6574HRR4LTIElOi1
1/HgnP1+htyvNSOseajPYd7Em4PQqkX4
1VjxOywOo1pPt84eyW9U12eWy1hGlHf8
rvvUIb3/Z2UvHzUfZi3Vmsvfm7r64BqN
PCoPh7GsGiDAAAAACLDeiNRSMG8AAHKB
 KO4AQDNZy4LscRn+wIAAAAABFla"""
import base64,lzma;sing=lzma.decompress(base64.b64decode(s)).decode().splitlines

print(sing()[0], '99 bottles of beer on the wall, 99 bottles of beer.')
print(sing()[199], 'Go to the store and buy some more, 99 bottles of beer on the wall.')