# Number to digit tiers
# https://www.codewars.com/kata/586bca7fa44cfc833e00005c/train/python

# 나의 풀이
def create_array_of_tiers0(n):
    answer = []
    tmp = ''
    for i in str(n):
        tmp += i
        answer.append(tmp)
    return answer

def create_array_of_tiers(n):
    return [str(n)[:i] for i in range(1, len(str(n))+1)]

# 다른 사람의 풀이
from itertools import accumulate
def create_array_of_tiers2(n):
    return list(accumulate(str(n)))

print(create_array_of_tiers(420), ["4", "42", "420"])
print(create_array_of_tiers(2017), ["2", "20", "201", "2017"])
print(create_array_of_tiers(2010), ["2", "20", "201", "2010"])
print(create_array_of_tiers(4020), ["4", "40", "402", "4020"])
print(create_array_of_tiers(80200), ["8", "80", "802", "8020", "80200"])