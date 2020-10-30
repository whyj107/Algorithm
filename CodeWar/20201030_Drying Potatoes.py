# Drying Potatoes
# https://www.codewars.com/kata/58ce8725c835848ad6000007/train/python

def potatoes(p0, w0, p1):
    return w0 * (100 - p0) // (100 - p1)

def dotest(p0, w0, p1, exp):
    print(potatoes(p0, w0, p1), exp)

dotest(82, 127, 80, 114)
dotest(93, 129, 91, 100)