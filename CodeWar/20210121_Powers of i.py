# Powers of i
# https://www.codewars.com/kata/5a97387e5ee396e70a00016d/train/python

# 나의 풀이
def pofi(n):
    tmp = ['1', 'i', '-1', '-i']
    return tmp[n%4]

# 다른 사람의 풀이
def pofi1(n):
    return {0:"1", 1:"i", 2:"-1", 3:"-i"}[n % 4]

def pofi2(n):
    return ['1','i','-1','-i'][n%4]

print(pofi(0), '1');
print(pofi(1), 'i');
print(pofi(2), '-1');
print(pofi(3), '-i');
print(pofi(4), '1');
print(pofi(5), 'i');
print(pofi(6), '-1');
print(pofi(7), '-i');
print(pofi(8), '1');
print(pofi(9), 'i');
print(pofi(10), '-1');