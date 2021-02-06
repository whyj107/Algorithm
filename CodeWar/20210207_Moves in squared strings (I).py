# Moves in squared strings (I)
# https://www.codewars.com/kata/56dbe0e313c2f63be4000b25/train/python

# 나의 풀이
def vert_mirror(strng):
    return '\n'.join(i[::-1] for i in strng.split('\n'))

def hor_mirror(strng):
    return '\n'.join(strng.split('\n')[::-1])

def oper(fct, s):
    return fct(s)

# 다른 사람의 풀이
def vert_mirror1(strng):
    return map(reversed, strng)
def hor_mirror1(strng):
    return reversed(strng)
def oper1(fct, s):
    return '\n'.join(map(''.join, fct(s.split('\n'))))


print(oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"),
            "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw")

print(oper(vert_mirror, "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx"),
            "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP")
print(oper(hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt"), "yeCt\nCSbg\nJVhv\nlVHt")
print(oper(hor_mirror, "njMK\ndbrZ\nLPKo\ncEYz"), "cEYz\nLPKo\ndbrZ\nnjMK")
