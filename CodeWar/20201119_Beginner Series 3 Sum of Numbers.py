# Beginner Series #3 Sum of Numbers
# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

# 나의 풀이
def get_sum(a,b):
    return sum(i for i in range(min(a, b), max(a, b)+1, 1))

# 다른 사람의 풀이
def get_sum1(a,b):
    return sum(range(min(a,b), max(a,b)+1))

print(get_sum(0,1),1)
print(get_sum(0,-1),-1)