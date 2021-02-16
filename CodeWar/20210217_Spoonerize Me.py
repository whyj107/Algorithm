# Spoonerize Me
# https://www.codewars.com/kata/56b8903933dbe5831e000c76/train/python

# 나의 풀이
def spoonerize(words):
    words = words.split()
    w0, w1 = words[0], words[-1]
    words[0] = w1[:1]+w0[1:]
    words[-1] = w0[:1]+w1[1:]
    return ' '.join(word for word in words)

# 다른 사람의 풀이
def spoonerize1(words):
    a, b = words.split()
    return '{}{} {}{}'.format(b[0], a[1:], a[0], b[1:])

print(spoonerize("nit picking"), "pit nicking")
print(spoonerize("wedding bells"), "bedding wells")
print(spoonerize("jelly beans"), "belly jeans")
print(spoonerize("pop corn"), "cop porn")