# Strange mathematics
# https://www.codewars.com/kata/604517d65b464d000d51381f/train/python

# 나의 풀이
def strange_math(n, k):
    return sorted([str(i) for i in range(1, n+1)]).index(str(k)) + 1

def strange_math1(n, k):
    return sorted(map(str, range(1, n+1))).index(str(k)) + 1

# 다른 사람의 풀이
def strange_math2(n, k):
    return sorted(range(n+1), key=str).index(k)

print(strange_math(11, 2), 4)
print(strange_math(15, 5), 11)
print(strange_math(15, 15), 7)