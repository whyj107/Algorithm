# 문제
# ASCII85 Encoding & Decoding
# https://www.codewars.com/kata/5277dc3ff4bfbd9a36000c1c/train/python

# 나의 풀이
import base64
def toAscii85(data):
    return base64.a85encode(data.encode("latin-1"), adobe=True).decode()

def fromAscii85(data):
    return base64.a85decode(data, adobe=True).decode("latin-1")

if __name__ == '__main__':
    print(toAscii85('easy')=='<~ARTY*~>')
    print(toAscii85('somewhat difficult')=='<~F)Po,GA(E,+Co1uAnbatCif~>')

    print(fromAscii85('<~ARTY*~>')=='easy')
    print(fromAscii85('<~F)Po,GA(E,+Co1uAnbatCif~>')=='somewhat difficult')