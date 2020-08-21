# 문제
# Largest product in a series
# https://www.codewars.com/kata/529872bdd0f550a06b00026e/train/python

# 나의 풀이
def greatest_product(n):
    ans = 0
    for i in range(len(n)-4):
        tmp = int(n[i])*int(n[i+1])*int(n[i+2])*int(n[i+3])*int(n[i+4])
        ans = max(tmp, ans)
    return ans

# 다른 사람의 풀이
from itertools import islice
from functools import reduce

def greatest_product1(n):
    numbers=[int(value) for value in n]
    result=[reduce(lambda x,y: x*y, islice(numbers, i, i+5), 1) for i in range(len(numbers)-4)]
    return max(result)

if __name__ == '__main__':
    print(greatest_product("123834539327238239583"), 3240)
    print(greatest_product("395831238345393272382"), 3240)
    print(greatest_product("92494737828244222221111111532909999"), 5292)
    print(greatest_product("92494737828244222221111111532909999"), 5292)
    print(greatest_product("02494037820244202221011110532909999"), 0)