# Gravity Flip
# https://www.codewars.com/kata/5f70c883e10f9e0001c89673/train/python

# 나의 풀이
def flip(d, a):
    return sorted(a) if d == 'R' else sorted(a, reverse=True)

# 다른 사람이 풀이
def flip1(d,a):
    return sorted(a, reverse=d=='L')

print(flip('R', [3, 2, 1, 2]), [1, 2, 2, 3])
print(flip('L', [1, 4, 5, 3, 5]), [5, 5, 4, 3, 1])
