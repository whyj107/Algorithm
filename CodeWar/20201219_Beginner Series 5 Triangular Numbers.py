# Beginner Series #5 Triangular Numbers
# https://www.codewars.com/kata/56d0a591c6c8b466ca00118b/train/python

# 풀이
def is_triangular(t):
    # 피타고라스 형태를 이용하여 구하는 한 변의 길이
    x = int((t*2)**0.5)
    return t == x*(x+1)/2

def is_triangular1(t):
    return (8 * t + 1)**0.5 % 1 == 0

print(is_triangular(1), True)
print(is_triangular(3), True)
print(is_triangular(6), True)
print(is_triangular(10), True)
print(is_triangular(15), True)
print(is_triangular(21), True)
print(is_triangular(28), True)
print(is_triangular(2), False)
print(is_triangular(7), False)
print(is_triangular(14), False)
print(is_triangular(27), False)