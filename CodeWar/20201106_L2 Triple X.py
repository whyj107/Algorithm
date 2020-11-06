# L2: Triple X
# https://www.codewars.com/kata/568dc69683322417eb00002c/train/python

# 나의 풀이
def triple_x(s):
    return s.find("x") == s.find("xxx") if s.find("x") != -1 else False

# 다른 사람의 풀이
def triple_x0(s: str) -> bool:
    return 0 <= s.find("x") == s.find("xxx")

print(triple_x(""), False)
print(triple_x("there's no XXX here"), False)
print(triple_x("abraxxxas"), True)
print(triple_x("xoxotrololololololoxxx"), False)
print(triple_x("soft kitty, warm kitty, xxxxx"), True)
print(triple_x("softx kitty, warm kitty, xxxxx"), False)
