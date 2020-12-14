# How many days are we represented in a foreign country?
# https://www.codewars.com/kata/58e93b4706db4d24ee000096/train/python

# 문제 자체를 이해하기 어려워서 풀지 못하였다.
# 다른 사람의 풀이를 보고 문제를 이해했다.
# 그래서 kata 8 짜리 문제를 풀었지만 sum(a)로 끝나는 문제여서 올리지는 않는다.

# 문제 풀이
def days_represented(a):
    return len({i for x, y in a for i in range(x, y + 1)})

def days_represented1(trips):
    arr = [0] * 365
    for a, b in trips:
        arr[a:b + 1] = [1] * (b - a + 1)
    return sum(arr)

print(days_represented([[10, 15], [25, 35]]), 17)
print(days_represented([[2, 8], [220, 229], [10, 16]]), 24)