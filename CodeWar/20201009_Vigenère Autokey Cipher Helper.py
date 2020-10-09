# 문제
# Vigenère Autokey Cipher Helper
# https://www.codewars.com/kata/52d2e2be94d26fc622000735/solutions

# 문제를 이해하기 힘들다.

class VigenereAutokeyCipher:
    def __init__(self, key, abc):
        self.key = key
        self.abc = abc
        self.alle = len(abc)

    def cipher(self, s, m):
        output, keyarr = '', list(self.key)
        for char in s:
            try:
                output += self.abc[(self.abc.index(char) + self.abc.index(keyarr.pop(0)) * (-1, 1)[m]) % self.alle]
                keyarr.append((output[-1], char)[m])
            except ValueError:
                output += char
        return output

    def encode(self, s):
        return self.cipher(s, 1)

    def decode(self, s):
        return self.cipher(s, 0)