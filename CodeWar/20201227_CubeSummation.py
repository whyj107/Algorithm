# CubeSummation
# https://www.codewars.com/kata/550e9fd127c656709400024d/train/python

# 나의 풀이
def cube_sum(n, m):
    return sum(i**3 for i in range(min(n, m)+1, max(n, m)+1))

# 다른 사람의 풀이
def cube_sum1(n, m):    return sum([(i+1)**3 for i in range(min(n,m),max(n,m))])

print(cube_sum(5, 0), 225)
print(cube_sum(2, 3), 27)
print(cube_sum(0, 4), 100)