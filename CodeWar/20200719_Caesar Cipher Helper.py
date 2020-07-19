# 문제
# Caesar Cipher Helper

# 나의 풀이
class CaesarCipher(object):
    def __init__(self, shift):
        self.alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.shift = shift

    def encode(self, st):
        return ''.join([self.alpha[(self.alpha.index(i.upper())+self.shift)%26] if i.upper() in self.alpha else i for i in st])

    def decode(self, st):
        return ''.join([self.alpha[(self.alpha.index(i.upper())-self.shift)%26] if i.upper() in self.alpha else i for i in st])

# 다른 사람의 풀이
from string import maketrans
class CaesarCipher1(object):

    def __init__(self, shift):
        self.alpha = "abcdefghijklmnopqrstuvwxyz".upper()
        self.newalpha = self.alpha[shift:] + self.alpha[:shift]

    def encode(self, str):
        t = maketrans(self.alpha, self.newalpha)
        return str.upper().translate(t)

    def decode(self, str):
        t = maketrans(self.newalpha, self.alpha)
        return str.upper().translate(t)

if __name__ == '__main__':
    c = CaesarCipher(5);

    print(c.encode('Codewars')=='HTIJBFWX');
    print(c.decode('HTIJBFWX')=='CODEWARS');