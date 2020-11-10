# Automorphic Number (Special Numbers Series #6)
# https://www.codewars.com/kata/5a58d889880385c2f40000aa/train/python

# 나의 풀이
def automorphic(n):
    return "Automorphic" if str(pow(n, 2)).endswith(str(n)) else "Not!!"

# 다른 사람의 풀이
def automorphic1(n):
    return "Automorphic" if str(n*n).endswith(str(n)) else "Not!!"

print(automorphic(1), "Automorphic")
print(automorphic(3), "Not!!")
print(automorphic(6), "Automorphic")
print(automorphic(9), "Not!!")
print(automorphic(25), "Automorphic")
print(automorphic(53), "Not!!")
print(automorphic(76), "Automorphic")
print(automorphic(95), "Not!!")
print(automorphic(625), "Automorphic")
print(automorphic(225), "Not!!")
