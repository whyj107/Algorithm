# Filling an array (part 1)
# https://www.codewars.com/kata/571d42206414b103dc0006a1/train/python

# 나의 풀이
def arr(n = 0):
        return [i for i in range(n)]

# 다른 사람의 풀이
def arr(n=0):
    return list(range(n))

print(arr(4), [0, 1, 2, 3])
print(arr(0), [])
print(arr(), [])