# Count the Digit
# https://www.codewars.com/kata/566fc12495810954b1000030/train/python

# 나의 풀이
def nb_dig(n, d):
    return sum(str(i**2).count(str(d)) for i in range(n+1))

# 다른 사람의 풀이
def nb_dig1(n, d):
    return sum(str(i*i).count(str(d)) for i in range(n+1))

print(nb_dig(10, 1), 4)
print(nb_dig(25, 1), 11)
print(nb_dig(5750, 0), 4700)
print(nb_dig(11011, 2), 9481)
print(nb_dig(12224, 8), 7733)
print(nb_dig(11549, 1), 11905)