# Unique string characters
# https://www.codewars.com/kata/5a262cfb8f27f217f700000b/train/python

# 나의 풀이
def solve(a,b):
    c = []
    for i in a:
        if i not in b:
            c.append(i)
    for i in b:
        if i not in a:
            c.append(i)
    return ''.join(c)

# 다른 사람의 풀이
def solve1(a,b):
    s = set(a)&set(b)
    return ''.join(c for c in a+b if c not in s)

def solve2(a,b):
    return "".join([c for c in a if not c in b]+[c for c in b if not c in a])

print(solve("xyab","xzca"),"ybzc")
print(solve("xyabb","xzca"),"ybbzc")
print(solve("abcd","xyz"),"abcdxyz")
print(solve("xxx","xzca"),"zca")